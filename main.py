import random
import time
import json

def generate_simulated_record(record_id):
    """
    Generates a simulated data record.
    Introduces errors randomly to simulate real-world data quality issues.
    """
    record = {
        "id": record_id,
        "timestamp": int(time.time()),
        "value": random.randint(100, 1000)
    }
    # Simulate a common data quality issue: non-numeric value where numeric is expected
    if random.random() < 0.2:  # 20% chance of a bad value
        record["value"] = random.choice(["ERROR_STR", None, "123a"])
    # Simulate a missing field
    if random.random() < 0.1: # 10% chance of missing timestamp
        del record["timestamp"]
    return record

def process_record(record):
    """
    Attempts to process a single data record.
    This function is designed to be 'failure-prone' to expose issues.
    """
    try:
        record_id = record.get("id")
        timestamp = record.get("timestamp")
        value = record.get("value")

        if timestamp is None:
            raise ValueError(f"Record {record_id}: Missing timestamp field.")
        if not isinstance(timestamp, int):
            raise TypeError(f"Record {record_id}: Timestamp is not an integer.")

        # Attempt to convert value to integer, expecting potential errors
        processed_value = int(value)
        
        # Simulate some processing logic
        result = processed_value * 2
        return {"status": "SUCCESS", "id": record_id, "processed_result": result}
    except (ValueError, TypeError, KeyError) as e:
        # This is where the 'hataya açık' (failure-prone) design shines.
        # We catch expected errors and log them, rather than crashing the whole pipeline.
        return {"status": "FAILED", "id": record.get("id", "UNKNOWN"), "error": str(e), "original_record": record}
    except Exception as e:
        # Catch any unexpected errors as well
        return {"status": "FAILED", "id": record.get("id", "UNKNOWN"), "error": f"Unexpected error: {str(e)}", "original_record": record}

def run_pilot_project(num_records=20):
    """
    Runs a small pilot project to test data processing logic against
    potentially faulty data. This simulates a controlled environment
    to learn about data quality and processing robustness.
    """
    print(f"--- Starting Pilot Project: Processing {num_records} records ---")
    successful_records = []
    failed_records = []

    for i in range(num_records):
        print(f"\nProcessing record {i+1}...")
        raw_record = generate_simulated_record(i + 1)
        print(f"  Generated: {json.dumps(raw_record)}")

        processing_result = process_record(raw_record)

        if processing_result["status"] == "SUCCESS":
            successful_records.append(processing_result)
            print(f"  SUCCESS: {json.dumps(processing_result)}")
        else:
            failed_records.append(processing_result)
            print(f"  FAILED: {json.dumps(processing_result)}")
        
        # Simulate a small delay for streaming feel
        time.sleep(0.1) 

    print("\n--- Pilot Project Summary ---")
    print(f"Total records processed: {num_records}")
    print(f"Successful records: {len(successful_records)}")
    print(f"Failed records: {len(failed_records)}")

    if failed_records:
        print("\nDetails of Failed Records (for analysis and learning):")
        for failure in failed_records:
            print(f"  - ID: {failure['id']}, Error: {failure['error']}, Original: {json.dumps(failure['original_record'])}")
    else:
        print("No records failed processing. Good job, or not enough faulty data generated!")

    print("\n--- Pilot Project Finished ---")

if __name__ == "__main__":
    run_pilot_project(num_records=20) # Run with a small number of records for the pilot
