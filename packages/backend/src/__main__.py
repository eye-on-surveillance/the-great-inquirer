import logging

from dotenv import find_dotenv, load_dotenv
from preprocessor import create_db_from_youtube_urls_and_pdfs, create_embeddings

load_dotenv(find_dotenv())

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main():
    cj_json_directory = "json_cj_directory"
    fc_json_directory = "json_fc_directory"
    minutes_directory = "minutes_pdfs"
    agendas_directory = "minutes_pdfs"
    print(f"Preprocessing videos, agendas, and minutes to generate a cache.")
    general_embeddings, in_depth_embeddings, voting_embeddings = create_embeddings()

    # create_db_from_fc_youtube_urls(FC_INPUT_VIDEO_URLS)
    create_db_from_youtube_urls_and_pdfs(
        fc_json_directory,
        cj_json_directory,
        minutes_directory,
        agendas_directory,
        general_embeddings,
        in_depth_embeddings,
        voting_embeddings,
    )


if __name__ == "__main__":
    main()
