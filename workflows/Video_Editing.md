### สรุป Workflow งาน Video Editing + Color Grading แบบมืออาชีพ

## 1. เตรียมไฟล์ (Media Management)

```text
SD Card
   ↓
SSD Working Drive
   ↓
Backup Drive
```

โครงสร้างโฟลเดอร์:

```text
Project_Name
├── Footage
├── Audio
├── Graphics
├── Project Files
├── Proxies
├── Exports
└── Archive
```

ใช้ Sigma Indexing เพื่อค้นหาไฟล์ได้ทันที เช่น

```text
*.mp4
*.wav
Drone
Interview
```

---

## 2. Workflow การตัดต่อวิดีโอ

```text
Import
  ↓
Organize
  ↓
Proxy Generation
  ↓
Rough Cut
  ↓
Fine Cut
  ↓
Color Grade
  ↓
Audio Mix
  ↓
Export
  ↓
QC
  ↓
Archive
```

### Rough Cut
- เลือกช็อต
- เรียงลำดับเรื่อง
- ตัดส่วนเกินออก

### Fine Cut
- Transition
- Motion Graphics
- B-Roll
- Titles

### Audio
- ลด Noise
- EQ
- Compression
- ปรับ Music

---

## 3. Workflow การ Color Grading

```text
Color Management
      ↓
Primary Correction
      ↓
Shot Matching
      ↓
Secondary Correction
      ↓
Creative Look
      ↓
Skin Tone
      ↓
Noise Reduction
      ↓
Final QC
```

---

## 4. Node Tree แนะนำ

### สำหรับงานทั่วไป

```text
01 Noise Reduction
        ↓
02 Input CST
        ↓
03 White Balance
        ↓
04 Exposure & Contrast
        ↓
05 Shot Match
        ↓
06 Skin Tone
        ↓
07 Creative Look
        ↓
08 Vignette
        ↓
09 Film Grain
        ↓
10 Output CST
```

---

## 5. Node Tree ระดับ Professional

```text
NR
 ↓
Input CST
 ↓
Balance
 ↓
Contrast
 ↓
Look Creation
 ├── Skin
 ├── Sky
 ├── Vegetation
 └── Windows
 ↓
Look Refinement
 ↓
Grain
 ↓
Output CST
```

แนวคิด:

```text
Technical Fix
      ↓
Matching
      ↓
Creative Grade
      ↓
Finishing
```

---

## 6. ลำดับการเกรดสีที่ถูกต้อง

### ก่อน

❌ ใส่ LUT ก่อนแก้ Exposure

### หลัง

✅ Exposure → White Balance → Match → Look

```text
Exposure
   ↓
White Balance
   ↓
Contrast
   ↓
Matching
   ↓
Creative Look
```

---

## 7. การจัดการ LUT และ PowerGrade

```text
Color
├── LUTs
├── PowerGrades
├── Reference Stills
├── Resolve Projects
└── Exports
```

ตัวอย่างค้นหาด้วย Sigma:

```text
Rec709
Film LUT
Kodak
PowerGrade
```

---

## Workflow ที่แนะนำที่สุดสำหรับ DaVinci Resolve

```text
Import
   ↓
Create Proxies
   ↓
Edit
   ↓
NR
   ↓
Input CST
   ↓
Balance
   ↓
Contrast
   ↓
Match Shots
   ↓
Creative Look
   ↓
Skin Tone
   ↓
Grain
   ↓
Output CST
   ↓
Export
   ↓
Archive
```

นี่เป็น Workflow ที่ใกล้เคียงกับที่ Colorist มืออาชีพใช้จริงสำหรับงาน YouTube, Commercial, Music Video และ Documentary ทั่วไป โดยแยก "Technical" ออกจาก "Creative" อย่างชัดเจน ทำให้แก้งานภายหลังได้ง่ายมากครับ।
