import csv
import logging
import os
from django.db import transaction, IntegrityError
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

# Configure logging
load_dotenv()

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def get_log_file_path(base_name, dir_path, max_count=1000):
    log_file_path = os.path.join(dir_path, base_name)
    counter = 1
    while os.path.exists(log_file_path) and counter <= max_count:
        log_file_path = os.path.join(dir_path, f"{base_name}.{counter}")
        counter += 1
    return log_file_path

gbif_log_file = get_log_file_path('gbif_backbone_import.log', LOG_DIR)

logging.basicConfig(level=logging.INFO)  # Changed to INFO to log all output
file_handler = RotatingFileHandler(gbif_log_file, maxBytes=1024*1024*5, backupCount=5)  # 5MB per file
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_handler)

def parse_tsv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            yield row

def save_batch(batch):
    from gbif.models import Taxon
    try:
        with transaction.atomic():
            for row in batch:
                Taxon.objects.create(
                    taxon_id=row['taxonID'],
                    dataset_id=row['datasetID'],
                    parent_name_usage_id=row.get('parentNameUsageID', None),
                    accepted_name_usage_id=row.get('acceptedNameUsageID', None),
                    original_name_usage_id=row.get('originalNameUsageID', None),
                    scientific_name=row['scientificName'],
                    scientific_name_authorship=row.get('scientificNameAuthorship', None),
                    canonical_name=row.get('canonicalName', None),
                    generic_name=row.get('genericName', None),
                    specific_epithet=row.get('specificEpithet', None),
                    infraspecific_epithet=row.get('infraspecificEpithet', None),
                    taxon_rank=row['taxonRank'],
                    name_according_to=row.get('nameAccordingTo', None),
                    name_published_in=row.get('namePublishedIn', None),
                    taxonomic_status=row['taxonomicStatus'],
                    nomenclatural_status=row.get('nomenclaturalStatus', None),
                    taxon_remarks=row.get('taxonRemarks', None),
                    kingdom=row.get('kingdom', None),
                    phylum=row.get('phylum', None),
                    class_field=row.get('class', None),  # Handle reserved keyword 'class'
                    order=row.get('order', None),
                    family=row.get('family', None),
                    genus=row.get('genus', None)
                )
            logging.info("Batch saved successfully.")
    except IntegrityError as e:
        logging.error(f"Error saving batch: {e}")
        for row in batch:
            logging.error(row)

def import_tsv(file_path, batch_size=1000):
    batch = []
    for row in parse_tsv(file_path):
        batch.append(row)
        if len(batch) >= batch_size:
            save_batch(batch)
            logging.info(f"Batch of {batch_size} records processed.")
            batch = []

    if batch:
        save_batch(batch)
        logging.info(f"Final batch of {len(batch)} records processed.")

def split_tsv(file_path, batch_size):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    output_dir = os.path.join(os.path.dirname(file_path), name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    counter = 1
    batch = []
    for row in parse_tsv(file_path):
        batch.append(row)
        if len(batch) >= batch_size:
            output_file_path = os.path.join(output_dir, f"{name}_{counter}{ext}")
            write_tsv(output_file_path, batch)
            logging.info(f"Created {output_file_path} with {batch_size} records.")
            batch = []
            counter += 1

    if batch:
        output_file_path = os.path.join(output_dir, f"{name}_{counter}{ext}")
        write_tsv(output_file_path, batch)
        logging.info(f"Created {output_file_path} with {len(batch)} records.")

def write_tsv(file_path, rows):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digidex.settings.dev')
    import django
    django.setup()

    file_path = '/home/raphael/Downloads/Taxon.tsv'
    batch_size = 1000  # Adjust as needed
    split_tsv(file_path, batch_size)
    # Now you can call import_tsv on the smaller files if necessary
    import_tsv(file_path)
