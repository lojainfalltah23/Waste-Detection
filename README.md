#  Waste Detection Project

![Waste Sample](images/waste.png)

This project uses **YOLOv8** for real-time waste detection in videos and integrates an **OpenAI Vision-Language Model (VLM)** for accurate classification verification.  
The VLM runs in **background threads** to keep video processing fast and smooth.

---

##  Main Features

- **Fast Detection (YOLOv8):** Detects waste objects in real time using deep learning.  
- **Smart Verification (VLM - GPT-4o-mini):** Refines detections and distinguishes complex cases (e.g., *mixed waste* vs. *concrete rubble*).  
- **High Performance:** VLM tasks run in background threads to avoid processing slowdowns.  
- **Organized Outputs:** Saves processed videos, detection snapshots, and detailed JSON logs with timestamps.

---

##  Project Structure

| File / Folder | Description |
| :-- | :-- |
| `main.py` | Main entry point of the application. |
| `.env` | Stores your **`OPENAI_API_KEY`** securely (required for VLM). |
| `config/settings.py` | Contains paths, thresholds, and the `CRITICAL_NEED_VLM` toggle. |
| `modules/` | Core logic files: `detector.py`, `vlm_analysis.py`, and `utils.py`. |
| `data/` | Stores input videos and the trained model (`best.pt`). |
| `outputs/` | Contains processed videos, logs, and detection snapshots. |

---

## Outputs

- **Processed Video:** Saved in `/outputs` with bounding boxes around detected waste.  
- **Detection Log (JSON):** Includes detected object, confidence score, and VLM verification status.  
- **Snapshots:** Each detected waste object is saved as an image in the `/outputs/snapshots` folder.

---
Note: Not all files are included in this public repo.

© 2025|wastw detection system
