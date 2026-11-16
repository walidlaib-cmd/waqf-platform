"""
مشغّل منصة 'وقف تاك' (WaqfTech)
نظام الوقف والاستثمار الإسلامي في الجزائر
وفقاً للقانون رقم 25-06 المؤرخ في 19 يوليو 2025 (الجريدة الرسمية رقم 47)
"""
import sys
import os
import uvicorn

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# إضافة مجلد backend إلى مسار بايثون
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

def main():
    print("=" * 80)
    print("      بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ - الجمهورية الجزائرية الديمقراطية الشعبية")
    print("              منصة 'وقف تاك' (WaqfTech) للأوقاف النقدية والاستثمار الإسلامي")
    print("=" * 80)
    print("  • المرجعية القانونية: القانون 25-06 الصادر بتاريخ 23 محرم 1447هـ / 19 يوليو 2025")
    print("  • العملة المعتمدة: الدينار الجزائري (DZD)")
    print("  • القرارات المنفذة:")
    print("     [✓] لكل واقف وقف مستقل بحساباته وسجلاته المفروزة")
    print("     [✓] قبول الوقف المؤبد والوقف المؤقت (المادتان 22 و 54)")
    print("     [✓] تمويل المشاريع من أموال الوقف وتمويل الأفراد جنباً إلى جنب")
    print("     [✓] إلغاء ضمان رأس المال عملاً بأحكام الشريعة ومبدأ الغنم بالغرم")
    print("     [✓] أجرة الناظر 10% من صافي الأرباح المحققة مع صندوق احتياطي للمخاطر (5%)")
    print("     [✓] فترة تراجع 72 ساعة للواقف لسحب كامل المبلغ بضغطة زر")
    print("     [✓] 8 مجالات وقفية و 5 قطاعات استثمارية و 7 صيغ تمويلية إسلامية")
    print("-" * 80)
    print("  🌐 الموقع وتطبيق الويب: http://localhost:8000")
    print("  📖 توثيق الـ API التفاعلي (Swagger): http://localhost:8000/docs")
    print("  ⚖️ بوابة الشفافية والحوكمة: http://localhost:8000/transparency")
    print("=" * 80)
    
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()

