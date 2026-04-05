import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
# นำเข้าไลบรารีสำหรับ AI (สมมติว่าเราฝึกโมเดลไว้แล้ว)
from sklearn.ensemble import RandomForestClassifier 

class OptoDigitalBiospeckle:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.images = self.load_image_sequence()
        # จำลองการโหลดโมเดล AI ที่ผ่านการ Train มาแล้ว
        self.ai_model = self._load_dummy_ai_model()

    def load_image_sequence(self):
        """โหลดลำดับภาพเลเซอร์สเปกเคิลเพื่อการวิเคราะห์ทางเวลา (Temporal Analysis)"""
        images = []
        if not os.path.exists(self.image_folder):
            print(f"Warning: Awaiting physical optical data in '{self.image_folder}'.")
            return images
        for filename in sorted(os.listdir(self.image_folder)):
            if filename.endswith((".jpg", ".png")):
                img_path = os.path.join(self.image_folder, filename)
                images.append(cv2.imread(img_path, cv2.IMREAD_GRAYSCALE))
        return np.array(images)

    def extract_optical_features(self):
        """คำนวณหา Temporal Speckle Contrast (จุดเชื่อมโยงระหว่าง Physics กับ Data)"""
        if len(self.images) < 2: return None
        
        mean_img = np.mean(self.images, axis=0)
        std_img = np.std(self.images, axis=0)
        mean_img[mean_img == 0] = 1 # ป้องกัน Error หารศูนย์
        
        contrast_map = std_img / mean_img
        return contrast_map

    def _load_dummy_ai_model(self):
        """ฟังก์ชันจำลองการโหลดโมเดล AI (Machine Learning)"""
        # ในการใช้งานจริง จะใช้ joblib.load('salmon_model.pkl')
        return "RandomForest_Pretrained"

    def predict_spoilage_with_ai(self, contrast_map):
        """ใช้ AI จำแนกความสดจากฟีเจอร์ของภาพ"""
        # สกัดค่าคุณลักษณะ (Feature Extraction) เพื่อส่งให้ AI
        mean_activity = np.mean(contrast_map)
        variance_activity = np.var(contrast_map)
        
        print(f"--- Computer Vision Features ---")
        print(f"Mean Biospeckle Activity: {mean_activity:.4f}")
        print(f"Activity Variance: {variance_activity:.4f}")
        
        # จำลองการตัดสินใจของ AI (Classification)
        print(f"\n--- AI Classification Result ---")
        if mean_activity < 0.3:
            return "🟩 FRESH (Safe to consume)"
        elif mean_activity < 0.6:
            return "🟨 SEMI-FRESH (Consume soon)"
        else:
            return "🟥 SPOILED (High bacterial activity detected)"

    def show_heatmap(self, contrast_map):
        plt.figure(figsize=(8, 6))
        plt.title("Optical Biospeckle Activity (Processed via CV)")
        plt.imshow(contrast_map, cmap='inferno')
        plt.colorbar(label='Speckle Contrast / Activity Level')
        plt.axis('off')
        plt.show()

# ==========================================
# Workflow การรันโปรแกรม
# ==========================================
if __name__ == "__main__":
    system = OptoDigitalBiospeckle("./optical_data_input")
    
    if len(system.images) > 0:
        # 1. Computer Vision Process
        contrast_features = system.extract_optical_features()
        system.show_heatmap(contrast_features)
        
        # 2. AI Prediction Process
        prediction = system.predict_spoilage_with_ai(contrast_features)
        print(f"Status: {prediction}")
    else:
        print("System initialized. Ready to process coherent light image sequences.")
