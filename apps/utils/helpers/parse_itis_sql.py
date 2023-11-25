import re

def parse_and_export_sql_file(filename):
    with open(filename, 'r', encoding='ISO-8859-1') as file:
        content = file.read()

    # Split content based on the provided pattern
    segments = re.split(r'-- Data for Name: (\w+); Type: TABLE DATA; Schema: public; Owner: -', content)

    # Iterate over segments in pairs (entity name and SQL content)
    for idx in range(1, len(segments), 2):
        entity_name = segments[idx]
        sql_content = segments[idx + 1]

        output_filename = f"/home/raphael/taxonomy_{entity_name}.sql"

        with open(output_filename, 'w', encoding='ISO-8859-1') as output_file:
            output_file.write(f"-- Data for Name: {entity_name}; Type: TABLE DATA; Schema: public; Owner: -\n")
            output_file.write(sql_content)

    print(f"Exported {len(segments) // 2} SQL files.")
