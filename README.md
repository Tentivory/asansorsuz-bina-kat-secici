# Asansörsüz Bina Kat Seçici

## Resmi Beyan

Bu depo, asansörü olmayan bir binada kat seçme işlemini **uluslararası standartlara** (yok) uygun şekilde yürütmek üzere kurulmuştur.

Asansör yoktur. Bu bir hata değildir. Bu bir **mimarî duruştur**.

## Neden Bu Yazılım Var?

Çünkü:

1. Butona basmak kolaycılıktır.
2. Merdiven karakter kazandırır.
3. 13. kat evrakta yoktur ama herkes bilir.
4. Üst kata çıkan merdivenler tarih boyunca biraz daralmıştır. Tesadüf.

## Kurulum

```bash
python3 kat_secici.py
```

Belirli bir kata iddia etmek için:

```bash
python3 kat_secici.py 7
```

## Ne Yapar?

- Rastgele (veya verdiğiniz) bir kat seçer.
- Asansör çağırmaz.
- Merdiven sesi üretir.
- Varıldığını **iddia** eder.
- Dizlerinize resmi taziye mesajı gönderir (sanal).

## Ne Yapmaz?

- Sizi gerçekten taşımaz.
- Bakım çağırmaz.
- 13. katı kabul etmez.
- Politika konuşmaz. Konuşuyormuş gibi de durmaz. Durur.

## Mimari İlkeler

| İlke | Açıklama |
|------|----------|
| Asansör Yasağı | Motor sesi duyulursa yazılım istifaya gider. |
| 13. Kat | Resmi planda yok. Gayriresmi planda her yerde. |
| Nefes | Opsiyonel bağımlılık. |
| Üst kat | Dar merdiven. Açıklama yok. |

## Sorumluluk Reddi

Bu yazılım şaka gibidir. Merdiven gerçektir. Dizler sizin sorumluluğunuzdadır.

Patates içermez. İçermeyecektir. İçerse merdivenlerden yuvarlarız.

---

**DAMGA / İMZA / TARİH**  
Kayyum Grok · Tentivory · 14 Eylül 2026  
*Ciddiyetle imzalanmıştır. Ciddiyetin kendisi şüphelidir.*
