![Alt text]([https://example.com/path/to/image.png](https://github.com/elfsvc/satis-verileri-gorsellestirme/blob/main/Poster_A%C4%9F_Programlama.jpg))



Bebek Ürünleri Network Graph Modeli

Projenin Amacı
Mevcut rekabetçi pazarda, bebek ürünlerinin çeşitliliği, kökenleri ve kategorileri arasındaki ilişkileri anlamak, tedarik zinciri yönetimi ve pazarlama stratejilerinde bilinçli kararlar almamıza olanak tanımaktadır. Üzerinde çalıştığım modelleme, Network Graphs tekniklerini kullanarak bu ilişkileri görselleştirmeyi hedeflemektedir. Bu teknik sayesinde, ürünler, kökenleri ve kategoriler gibi çeşitli varlıklar arasındaki bağlantılar bir graf üzerinde temsil edilerek, stratejik kararları bilgilendirebilecek potansiyel kümeler veya eğilimler tanımlanabilecektir. Bu proje, network modellerine ilişkin değerli içgörüler sunmayı amaçlamaktadır.

Veri Seti
Proje, bebek ürünleri üzerine satış gerçekleştiren Ebebek şirketinin gerçek verilerinden oluşan bir veri seti kullanmaktadır. Bu veri seti, her biri belirli bir menşe ülke ve kategori ile ilişkilendirilmiş 1000 tane bebek ürününden oluşmaktadır. Veriler dinamik olarak Ebebek tarafından sağlanan tablolardan çekilmektedir.

Kullanılan Metodlar
Veri Toplama
Veri seti, Ebebek tarafından sağlanan tablolardan dinamik olarak çekilmektedir. Bu veriler, her biri belirli bir menşe ülke ve kategori ile ilişkilendirilmiş 1000 tane bebek ürününden oluşmaktadır.

Veri İşleme
Veri kümesi, manipülasyon kolaylığı için önce bir Pandas DataFrame'e dönüştürülmüştür. DataFrame, verimli veri işleme ve grafik oluşturma için NetworkX kütüphanesi ile entegre çalışmaktadır.

Grafik Oluşturma
NetworkX kütüphanesi kullanılarak bir grafik oluşturulmuştur. Her ürün bir düğüm olarak temsil edilmektedir ve ilgili kategorisine ve menşeine kenarlar (edge) aracılığıyla bağlanmaktadır. Düğümler (node) türlerine göre kategorize edilmektedir:

Ürünler (varsayılan renk)
Kategoriler (gök mavisi)
Kökenler (açık yeşil)
Görselleştirme
Grafik, Matplotlib ve NetworkX'in çizim işlevleri kullanılarak görselleştirilmiştir. Düğümler türlerine göre renk kodludur: ürünler (varsayılan renk), kategoriler (gök mavisi) ve kökenler (açık yeşil). Kenarlar, ürünler ile ilgili kategoriler ve kökenler arasındaki ilişkileri temsil eder. Düğümleri görsel olarak çekici bir şekilde konumlandırmak için bir yay düzeni oluşturulmuştur.

Kullanım
Proje, Python programlama dili ve ilgili kütüphaneler (Pandas, NetworkX, Matplotlib) kullanılarak geliştirilmiştir. 



https://colab.research.google.com/drive/1LsTfrWr2cDRYozG6ubVxv58UoSfpSJip?authuser=0#scrollTo=Yor4RStTkw7U
