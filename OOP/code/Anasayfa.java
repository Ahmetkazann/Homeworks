// 19010011039 Ahmet Emin Kazan 
// kursiyer.txt dosyasında en alt kısımda * bulunmalı
//not defteri bu formattadır. arrayliwsti doldururken * ifadesini gördükçe doldurduğu için son kursiyeri atlamaması icindir.
package nesne_odev2;
// error exist hatası muhtemelen filereader sınıfından kaynaklı kodun calısmasına herhangi bir etkisi yok.
import java.io.*;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class Anasayfa {

    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);
        	FileReader fr = new FileReader("C:\\Users\\ahmet\\Desktop\\Workspace\\kursiyer.txt");
            FileReader fr2 = new FileReader("C:\\Users\\ahmet\\Desktop\\Workspace\\kurs.txt");
            BufferedReader br = new BufferedReader(fr);
            ArrayList<String> kursiyerbilgileri = new ArrayList<>();
            ArrayList<String> kursbilgileri = new ArrayList<>();
            String[] kursiyer = null;
            String[] kursiyerinkurslari;
            int kursid;
            String kursad;
            //ArrayList<Kurs> kurslar2 = new ArrayList<Kurs>();
            ArrayList<Kursiyer> kursiyerler = new ArrayList<Kursiyer>();
            ArrayList<Kurs> tumkurslar = new ArrayList<Kurs>();
            
            String line;
            while ((line = br.readLine()) != null) {
                kursiyerbilgileri.add(line);
            }
            br = new BufferedReader(fr2);
//            while ((line = br.readLine()) != null) {
//                kursbilgileri.add(line);
//            }
            kursbilgileri.clear();
            for (String bilgi : kursiyerbilgileri) {
                //System.out.println(bilgi);
                //System.out.println(kursbilgileri);
                if(bilgi.contains("*")) {
                	ArrayList<Kurs> kurslar2 = new ArrayList<Kurs>();
                	if(!kursbilgileri.isEmpty()) {
                		for(int i = 0; i < kursbilgileri.size();i+=2) {
                			Kurs gecicikurs = new Kurs(Integer.parseInt(kursbilgileri.get(i)), kursbilgileri.get(i + 1));
                			kurslar2.add(gecicikurs);
                		}
                		System.out.println("kursiyereklendi");
                		Kursiyer gecicikursiyer = new Kursiyer(Integer.parseInt(kursiyer[0]), kursiyer[1], Integer.parseInt(kursiyer[2]), kurslar2);
                		kursiyerler.add(gecicikursiyer);

                	}
                	kursbilgileri.clear();
                	//kurslar2.clear();
                	//String[] operators = new String[] {"-","\\+","/","\\*","x","\\^","X"};
                	kursiyer = bilgi.split("\\+");
                	kursiyer[0] = kursiyer[0].replace("*", "");
                	//System.out.println(kursiyer[0] + "-" +kursiyer[1] + "-" +kursiyer[2]);
                	}
                if(bilgi.contains("%")) {
                	kursiyerinkurslari = bilgi.split("\\+");
                	kursiyerinkurslari[0] = kursiyerinkurslari[0].replace("%", "");
//                	System.out.println(kursiyerinkurslari[0] + "-" +kursiyerinkurslari[1]);
                	kursbilgileri.add(kursiyerinkurslari[0]);
                	kursbilgileri.add(kursiyerinkurslari[1]);
                }
            }
            kursbilgileri.clear();
            
            while ((line = br.readLine()) != null) {
                kursbilgileri.add(line);
                String[] kurs = line.split("\\+");
                Kurs gecicikurs = new Kurs(Integer.parseInt(kurs[0]), kurs[1]);
    			tumkurslar.add(gecicikurs);
            }
            
            
            for(int i = 0; i < kursiyerler.size();i++) {// txt dosyasından kursiyerler arraylistine aktarılan bilgiler
            	kursiyerler.get(i).BilgileriYazdir();
            }
            System.out.println("--------------------");
            for(int i = 0; i < tumkurslar.size();i++) { // txt dosyasından tumkurslar arraylistine aktarılan bilgiler
            	tumkurslar.get(i).BilgileriYazdir();
            }
//            for (String bilgi : kursbilgileri) {
//                System.out.println(bilgi);
//                
//            }
            br.close();
            while (true) {
                System.out.println("\n----- Menü -----");
                System.out.println("1- Kurs Ekle");
                System.out.println("2- Kurs Listele");
                System.out.println("3- Kurs Ara");
                System.out.println("4- Kurs Sil");
                System.out.println("5- Kursiyer Ekle");
                System.out.println("6- Kursiyer Ara");
                System.out.println("7- Kursiyer Sil");
                System.out.println("8- Kursiyerleri Listele");
                System.out.println("9- Kusiyerleri Ayrıntılı Listele");
                System.out.println("10- Kursiyerin Ödeyeceği Tutarı Hesapla");
                System.out.println("11- Çıkış");
                
                System.out.println("input : ");
                int secim = sc.nextInt();

                switch (secim) {
                    case 1:
                    	System.out.println("Eklenecek Kursun Id'sini Giriniz:");
                    	int geciciid = sc.nextInt();
                    	System.out.println("Eklenecek Kursun Adini Giriniz:");
                    	String geciciad = sc.next();
                    	boolean var = false;
                    	for(int i = 0; i < tumkurslar.size();i++) {
                    		if(tumkurslar.get(i).getKursId() == geciciid) {
                    			var = true;
                    			break;
                    		}
                    	}
                    	if(var == true) {
                			System.out.println("Bu Id'ye Sahip Baska Bir Kurs Var Menuye Donuluyor.");
                    		break;
                    	}
                    	else {
                    		Kurs gecicikurs = new Kurs(geciciid,geciciad);
                    		tumkurslar.add(gecicikurs);
                    		System.out.println(geciciid +" - " + geciciad + " - Bilgilerine Sahip Kurs Eklendi.");
                    		break;
                    	}
                    case 2:
                    	System.out.println("-------------------------------");
                    	System.out.println("Tum Kurslar Listeleniyor...");
                    	for(int i = 0; i < tumkurslar.size();i++) { // txt dosyasından tumkurslar arraylistine aktarılan bilgiler
                        	tumkurslar.get(i).BilgileriYazdir();
                        }
                    	break;

                    case 3:
                    	System.out.println("Aranacak Kursun Id'sini Giriniz:");
                    	int geciciid2 = sc.nextInt();
                    	boolean var2 = false;
                    	for(int i = 0; i < tumkurslar.size();i++) {
                    		if(tumkurslar.get(i).getKursId() == geciciid2) {
                    			var2 = true;
                    			System.out.println("Bu İd'de Kurs Bulundu: ");
                    			tumkurslar.get(i).BilgileriYazdir();
                    			break;
                    		}
                    	}
                    	if(var2==false) {
                    		System.out.println("Aranan Kurs Bulunamadi Menuye Donuluyor...");
                    	}
                    	break;

                    case 4:
                    	System.out.println("Aranacak Kursun Id'sini Giriniz:");
                    	int geciciid3 = sc.nextInt();
                    	boolean var3 = false;
                    	for(int i = 0; i < tumkurslar.size();i++) {
                    		if(tumkurslar.get(i).getKursId() == geciciid3) {
                    			var2 = true;
                    			System.out.println("Bu İd'de Kurs Bulundu Siliniyor...");
                    			tumkurslar.get(i).BilgileriYazdir();
                    			tumkurslar.remove(i);
                    			var3 = true;
                    			break;
                    		}
                    	}
                    	if(var3==false) {
                    		System.out.println("Silinmek İstenens Kurs Bulunamadi Menuye Donuluyor...");
                    	}

                    	break;

                    case 5:
                    	//gecicikurslar.clear();
                    	ArrayList<Kurs> gecicikurslar = new ArrayList<Kurs>();
                    	System.out.println("Eklenecek Kursiyerin Id:");
                    	int gecicikursiyerid = sc.nextInt();
                    	var = false;
                    	System.out.println("Eklenecek Kursiyerin Ad Soyad:");
                    	String gecicikursiyerad = sc.next();
                    	System.out.println("Eklenecek Kursiyerin Yas:");
                    	int gecicikursiyeryas = sc.nextInt();
                    	
                    	for(int i = 0; i < kursiyerler.size();i ++) {
                    		if(kursiyerler.get(i).getKursiyerId() == gecicikursiyerid) {
                    			var = true;
                    			System.out.println("Bu Id'de Kursiyer Var Menuye Donuluyor.");
                    		}
                    	}

                    	if(var == false) {
                    		
                    		int gecicikurssayisi;
                    		
                        	System.out.println("Eklenecek Kurs Sayisini Gir: ");
                        	gecicikurssayisi = sc.nextInt();
                        	for(int i = 0; i < gecicikurssayisi; i++) {
                        		System.out.println("Eklenecek Kursun Id'sini Giriniz:");
                            	int geciciid4 = sc.nextInt();
                            	System.out.println("Eklenecek Kursun Adini Giriniz:");
                            	String geciciad4 = sc.next();
                            	Kurs gecicikurs2 = new Kurs(geciciid4,geciciad4);
                        		gecicikurslar.add(gecicikurs2);
                        	}
                        	Kursiyer gecicikursiyer = new Kursiyer(gecicikursiyerid,gecicikursiyerad,gecicikursiyeryas,gecicikurslar);
                        	kursiyerler.add(gecicikursiyer);
                        	
                    	}
                    	break;
                    case 6:
                    	System.out.println("Aranacak Kursiyerin Id'sini Giriniz:");
                    	geciciid = sc.nextInt();
                    	var = false;
                    	for(int i = 0; i <kursiyerler.size();i++) {
                    		if(kursiyerler.get(i).getKursiyerId() == geciciid) {
                    			var = true;
                    			System.out.println("Bu İd'de Kursiyer Bulundu");
                    			kursiyerler.get(i).BilgileriYazdir();
                    			var = true;
                    			break;
                    		}
                    	}
                    	if(var==false) {
                    		System.out.println("Aranan İstenen Kursiyer Bulunamadi Menuye Donuluyor...");
                    	}
                    	
                    	
                    	break;
                    case 7:
                    	System.out.println("Silinecek Kursiyerin Id'sini Giriniz:");
                    	geciciid = sc.nextInt();
                    	var = false;
                    	for(int i = 0; i < kursiyerler.size();i++) {
                    		if(kursiyerler.get(i).getKursiyerId() == geciciid) {
                    			var = true;
                    			System.out.println("Bu İd'de Kursiyer Bulundu Siliniyor...");
                    			kursiyerler.get(i).BilgileriYazdir();
                    			kursiyerler.remove(i);
                    			var = true;
                    			break;
                    		}
                    	}
                    	if(var==false) {
                    		System.out.println("Silinmek İstenen Kursiyer Bulunamadi Menuye Donuluyor...");
                    	}
                    	break;
                    case 8:
                    	for(int i = 0; i <kursiyerler.size(); i++) {
                    		System.out.println(kursiyerler.get(i).getKursiyerId()+" - "+kursiyerler.get(i).getKursiyerAdSoyad()+" "+ kursiyerler.get(i).getKursiyerYas());
                    	}
                    	break;
                    case 9:
                    	for(int i = 0; i <kursiyerler.size(); i++) {
                    		kursiyerler.get(i).BilgileriYazdir();
                    	}
                    	break;
                    case 10:
                    	System.out.println("Borcu Hesaplanacak Kursiyerin İd'sini giriniz:");
                    	gecicikursiyerid = sc.nextInt();
                    	for(int i = 0; i<kursiyerler.size();i++) {
                    		if(kursiyerler.get(i).getKursiyerId() == gecicikursiyerid) {
                    			kursiyerler.get(i).BorcHesapla();
                    		}
                    	}
                    	break;
                    case 11:
                    	FileWriter myWriter = new FileWriter("C:\\Users\\ahmet\\Desktop\\Workspace\\kursiyer.txt");
                    	FileWriter myWriter2 = new FileWriter("C:\\Users\\ahmet\\Desktop\\Workspace\\kurs.txt");
                    	//myWriter.print("");
                    	for(int i = 0;i<kursiyerler.size();i++) {
                    		ArrayList<Kurs> temp = kursiyerler.get(i).getKurslar();
                    		//String[] operators = new String[] {"-","\\+","/","\\*","x","\\^","X"};
                    		myWriter.write("*");
                    		myWriter.write(Integer.toString(kursiyerler.get(i).getKursiyerId()));
                    		myWriter.write("+");
                    		myWriter.write(kursiyerler.get(i).getKursiyerAdSoyad());
                    		myWriter.write("+");
                    		myWriter.write(Integer.toString(kursiyerler.get(i).getKursiyerYas()));
                    		myWriter.write("\n");
                    		for(int j = 0; j<temp.size();j++) {
                    			myWriter.write("%");
                    			myWriter.write(Integer.toString(temp.get(j).getKursId()));
                    			myWriter.write("+");
                    			myWriter.write(temp.get(j).getKursAd());
                    			myWriter.write("\n");
                    		}
                    		
                    	}
                    	myWriter.write("*");
                        
                    	
                    	for(int i = 0;i<tumkurslar.size();i++) {
                    		myWriter2.write(Integer.toString(tumkurslar.get(i).getKursId()));
                    		myWriter2.write("+");
                    		myWriter2.write(tumkurslar.get(i).getKursAd());
                    		myWriter2.write("\n");
                    	}
                        myWriter.close();
                        myWriter2.close();
                        System.out.println("Program sonlandırıldı");
                        System.exit(0);
                        break;
                    default:
                        System.out.println("1-11 arasi sayi gir.");
                }
            }
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

