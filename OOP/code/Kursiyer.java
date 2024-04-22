// 19010011039 Ahmet Emin Kazan 
package nesne_odev2;
import java.util.ArrayList;

public class Kursiyer implements Hesaplama{
	private int kursiyerId;
	private String kursiyerAdSoyad;
	private int kursiyerYas;
	ArrayList<Kurs> kurslar = new ArrayList<Kurs>();
	
	public Kursiyer(int kursiyerId, String kursiyerAdSoyad, int kursiyerYas, ArrayList<Kurs> kurslar) {
		super();
		this.kursiyerId = kursiyerId;
		this.kursiyerAdSoyad = kursiyerAdSoyad;
		this.kursiyerYas = kursiyerYas;
		this.kurslar = kurslar;
	}

	public void BorcHesapla() {
		if(this.kurslar.size() == 1) {
			System.out.println("1 Kurs Alana İcin Herhangi Bir Kampanya Mevcut Degil");
		}
		
		else if(this.kurslar.size() == 2) {
			System.out.println("Kisinin Toplam Borcu:"+ (500 + 500*80/100));
		}
		
		else if(this.kurslar.size() == 3) {
			System.out.println("Kisinin Toplam Borcu:"+ (500*90/100 + 500*90/100 + 500*90/100));
		}
	}
	
	public void BilgileriYazdir() {
		System.out.println("kursiyer id: " + kursiyerId + " ad: " + kursiyerAdSoyad+ " yas: " + kursiyerYas);
		for(int i = 0; i < kurslar.size(); i++) {
			this.kurslar.get(i).BilgileriYazdir();
		}
	}

	public int getKursiyerId() {
		return kursiyerId;
	}

	public void setKursiyerId(int kursiyerId) {
		this.kursiyerId = kursiyerId;
	}

	public String getKursiyerAdSoyad() {
		return kursiyerAdSoyad;
	}

	public void setKursiyerAdSoyad(String kursiyerAdSoyad) {
		this.kursiyerAdSoyad = kursiyerAdSoyad;
	}

	public int getKursiyerYas() {
		return kursiyerYas;
	}

	public void setKursiyerYas(int kursiyerYas) {
		this.kursiyerYas = kursiyerYas;
	}

	public ArrayList<Kurs> getKurslar() {
		return kurslar;
	}

	public void setKurslar(ArrayList<Kurs> kurslar) {
		this.kurslar = kurslar;
	}


	
	
}
