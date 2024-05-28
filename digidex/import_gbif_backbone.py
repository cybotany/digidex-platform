import csv
import logging
import os
from django.db import transaction, IntegrityError
from dotenv import load_dotenv

# Configure logging
load_dotenv()
logging.basicConfig(filename='import_errors.log', level=logging.ERROR)

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
            batch = []

    if batch:
        save_batch(batch)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digidex.settings.dev')
    import django
    django.setup()
    
    file_path = '/home/raphael/Downloads/Taxon.tsv'
    import_tsv(file_path)
