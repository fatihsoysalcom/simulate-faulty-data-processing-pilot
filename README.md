# Simulate Faulty Data Processing Pilot

This example demonstrates a "failure-prone pilot project" approach to testing data processing logic. It simulates a stream of data, intentionally introducing errors like malformed values or missing fields. The processing function is designed to gracefully handle these errors, log failures, and continue processing, allowing developers to identify potential issues and learn about data quality challenges in a controlled, small-scale environment before implementing a full-scale solution like Apache Beam.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Run from your terminal: `python main.py`

## Original Article

This example accompanies the Turkish article: [Google Beam Öncesi Hataya Açık Bir Pilot Proje Nasıl Tasarlanır?](https://fatihsoysal.com/blog/google-beam-oncesi-hataya-acik-bir-pilot-proje-nasil-tasarlanir/).

## License

MIT — see [LICENSE](LICENSE).
