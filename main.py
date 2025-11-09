# main.py
import os
import sys
import datetime 

# Add paths to enable module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'config')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules')))

import config.settings as cfg
from modules.utils import setup_directories, export_json_log
from modules.detector import process_video

def main():
    """Main entry point for the application."""
    
    # Generate unique timestamp: YYYYMMDD_HHMM
    current_time_str = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    
    processed_video_filename = cfg.PROCESSED_VIDEO_FILE_PATTERN.format(timestamp=current_time_str)
    json_output_filename = cfg.JSON_OUTPUT_FILE_PATTERN.format(timestamp=current_time_str)

    print("===========================================================")
    print("         Waste Detection and VLM Analysis System")
    print(f"        VLM Status: {'Enabled' if cfg.CRITICAL_NEED_VLM else 'Disabled'}")
    print(f"        Output Tag: {current_time_str}")
    print("===========================================================")
    
    setup_directories(cfg.OUTPUT_DIR, cfg.SNAPSHOTS_SUBDIR)
    
    try:
        detection_records = process_video(processed_video_filename, json_output_filename)
        
        json_filepath = export_json_log(detection_records, cfg.OUTPUT_DIR, json_output_filename)
        
        print("\n===========================================================")
        print("Processing and Detection completed successfully.")
        print(f"Processed Video saved to: {os.path.join(cfg.OUTPUT_DIR, processed_video_filename)}")
        print(f"Data Log (JSON) saved to: {json_filepath}")
        print("===========================================================")
        
    except IOError as e:
        print(f"FATAL ERROR: Cannot open video file or device. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()