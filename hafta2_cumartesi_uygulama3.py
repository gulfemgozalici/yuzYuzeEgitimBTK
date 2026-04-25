# • Görev: Bir Robot sınıfı oluşturun.
# • Gereksinimler:
# • Her robotun bir isim özelliği olsun (__init__ ile alınacak).
# • Sınıf seviyesinde toplam_robot_sayisi değişkeni olsun ve her yeni robotta
# artsın.
# • selamla() adında bir instance metodu yazın; bu metot "Merhaba, ben
# [isim]" desin.
# • @classmethod ile robot_sayisini_sorgula() adında bir metot yazın; bu
# metot "Şu an dünyada X tane robot var" şeklinde cevap versin.

class Robot:
    toplam_robot_sayisi = 0
    def __init__(self, isim):
        self.isim = isim
        Robot.toplam_robot_sayisi += 1
    def selamla(isim):
        return f"Merhaba, ben {isim}"
    @classmethod
    def robot_sayisini_sorgula(cls):
        return f"Şu an dünyada {cls.toplam_robot_sayisi} tane robot var."

robot1 = Robot("Robot1")
robot2 = Robot("Robot2")
robot3 = Robot("Robot3")

print(Robot.robot_sayisini_sorgula())
