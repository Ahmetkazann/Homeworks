// 19010011039 Ahmet Emin Kazan 
package nesne_odev2;

public class Kurs{
	private int kursId;
	private String kursAd;
	public Kurs(int kursId, String kursAd) {
		super();
		this.kursId = kursId;
		this.kursAd = kursAd;
	}

	public void BilgileriYazdir() {
		System.out.println("kurs id: "+kursId + " kurs ad : " + kursAd);
	}

	public int getKursId() {
		return kursId;
	}

	public String getKursAd() {
		return kursAd;
	}

}
