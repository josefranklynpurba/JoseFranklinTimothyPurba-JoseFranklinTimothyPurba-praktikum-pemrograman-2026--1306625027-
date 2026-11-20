import math
import random
from array import array
from dataclasses import dataclass
from pathlib import Path

import pygame


LEBAR = 1050
TINGGI = 600
RADIUS_BOLA = 20
DIAMETER_BOLA = RADIUS_BOLA * 2
BATAS_KIRI = 70
BATAS_KANAN = 980
BATAS_ATAS = 80
BATAS_BAWAH = 510
POSISI_LUBANG = (
    (55, 65), (525, 65), (995, 65),
    (55, 525), (525, 525), (995, 525),
)
RADIUS_TANGKAP_LUBANG = 26
KECEPATAN_MAKS = 1800
SENSITIVITAS_TARIK = 12
FPS = 60

HIJAU_MEJA = (0, 138, 72)
PUTIH = (250, 250, 250)
EMAS = (248, 179, 35)
BIRU = (45, 127, 184)
KUNING = (254, 240, 11)
KAYU_GELAP = (77, 37, 17)
KAYU = (169, 105, 50)
KAYU_TERANG = (207, 151, 89)
UJUNG_STICK = (48, 36, 27)


@dataclass
class Bola:
    x: float
    y: float
    warna: tuple
    nama: str
    vx: float = 0
    vy: float = 0
    aktif: bool = True


def buat_suara_fallback(jenis):
    sample_rate = 22050
    durasi = 0.13 if jenis == "bola" else 0.18
    volume = 0.52 if jenis == "bola" else 0.42
    generator = random.Random(17 if jenis == "bola" else 29)
    sampel = array("h")

    for i in range(int(sample_rate * durasi)):
        waktu = i / sample_rate
        noise = generator.uniform(-1, 1)
        if jenis == "bola":
            envelope = math.exp(-waktu * 55)
            gelombang = (
                0.55 * math.sin(2 * math.pi * 410 * waktu)
                + 0.28 * math.sin(2 * math.pi * 790 * waktu)
                + 0.17 * math.sin(2 * math.pi * 1280 * waktu)
                + 0.32 * noise * math.exp(-waktu * 130)
            )
        else:
            envelope = math.exp(-waktu * 32)
            gelombang = (
                0.58 * math.sin(2 * math.pi * 175 * waktu)
                + 0.25 * math.sin(2 * math.pi * 360 * waktu)
                + 0.17 * noise * math.exp(-waktu * 75)
            )
        nilai = max(-32768, min(32767, int(32767 * volume * envelope * gelombang)))
        sampel.append(nilai)

    return pygame.mixer.Sound(buffer=sampel.tobytes())


def muat_suara(nama, jenis):
    folder = Path(__file__).resolve().parent
    for ekstensi in (".wav", ".ogg"):
        path_suara = folder / (nama + ekstensi)
        if path_suara.is_file():
            return pygame.mixer.Sound(str(path_suara))

    print(
        f"Rekaman {nama}.wav/.ogg belum ada; "
        f"memakai efek suara sintetis sementara."
    )
    return buat_suara_fallback(jenis)


def gambar_meja(layar, font_judul, font_petunjuk):
    layar.fill((24, 67, 45))
    pygame.draw.rect(layar, (93, 52, 29), (38, 48, 974, 494), border_radius=18)
    pygame.draw.rect(layar, HIJAU_MEJA, (50, 60, 950, 470))

    for posisi in POSISI_LUBANG:
        pygame.draw.circle(layar, (19, 20, 17), posisi, 24)

    judul = font_judul.render("SIMULASI BILIAR", True, PUTIH)
    petunjuk = font_petunjuk.render(
        "Klik bola putih, tarik ke belakang, lalu lepaskan untuk memukul.",
        True,
        PUTIH,
    )
    layar.blit(judul, (390, 12))
    layar.blit(petunjuk, (235, 558))


def gambar_bola(layar, bola):
    if not bola.aktif:
        return
    x = round(bola.x)
    y = round(bola.y)
    pygame.draw.circle(layar, (20, 48, 33), (x + 3, y + 4), RADIUS_BOLA)
    pygame.draw.circle(layar, bola.warna, (x, y), RADIUS_BOLA)
    pygame.draw.circle(layar, (55, 55, 55), (x, y), RADIUS_BOLA, 1)
    pygame.draw.circle(layar, (255, 255, 255), (x - 6, y - 7), 5)


def gambar_tongkat(layar, bola, arah_x, arah_y, tarikan=0):
    panjang = 320
    jarak_ujung = RADIUS_BOLA + 7 + min(tarikan, 180) * 0.22
    belakang_x = -arah_x
    belakang_y = -arah_y
    ujung = (
        bola.x + belakang_x * jarak_ujung,
        bola.y + belakang_y * jarak_ujung,
    )
    pangkal = (
        bola.x + belakang_x * (jarak_ujung + panjang),
        bola.y + belakang_y * (jarak_ujung + panjang),
    )
    tegak_x = -belakang_y
    tegak_y = belakang_x

    def titik(pusat, lebar, tanda):
        return (
            round(pusat[0] + tegak_x * lebar * tanda),
            round(pusat[1] + tegak_y * lebar * tanda),
        )

    pygame.draw.polygon(
        layar,
        KAYU_GELAP,
        [titik(ujung, 4, 1), titik(pangkal, 9, 1),
         titik(pangkal, 9, -1), titik(ujung, 4, -1)],
    )
    pygame.draw.polygon(
        layar,
        KAYU,
        [titik(ujung, 2.5, 1), titik(pangkal, 6, 1),
         titik(pangkal, 6, -1), titik(ujung, 2.5, -1)],
    )
    pygame.draw.line(layar, KAYU_TERANG, titik(ujung, 0, 1), titik(pangkal, 4, 1), 2)
    pygame.draw.line(layar, UJUNG_STICK, titik(ujung, 3, 1), titik(ujung, 3, -1), 3)


def bola_belum_berhenti(bola):
    return bola.aktif and math.hypot(bola.vx, bola.vy) > 8


def semua_bola_berhenti(bola_bola):
    return not any(bola_belum_berhenti(bola) for bola in bola_bola)


def perbarui_substep(bola_bola, dt, suara_bola):
    for bola in bola_bola:
        if not bola.aktif:
            continue

        bola.x += bola.vx * dt
        bola.y += bola.vy * dt

        if any(
            (bola.x - lubang_x) ** 2 + (bola.y - lubang_y) ** 2
            <= RADIUS_TANGKAP_LUBANG ** 2
            for lubang_x, lubang_y in POSISI_LUBANG
        ):
            bola.aktif = False
            bola.vx = 0
            bola.vy = 0
            suara_bola.play()
            continue

        if bola.x < BATAS_KIRI:
            bola.x = BATAS_KIRI
            if bola.vx < 0:
                bola.vx = -bola.vx * 0.96
                suara_bola.play()
        elif bola.x > BATAS_KANAN:
            bola.x = BATAS_KANAN
            if bola.vx > 0:
                bola.vx = -bola.vx * 0.96
                suara_bola.play()

        if bola.y < BATAS_ATAS:
            bola.y = BATAS_ATAS
            if bola.vy < 0:
                bola.vy = -bola.vy * 0.96
                suara_bola.play()
        elif bola.y > BATAS_BAWAH:
            bola.y = BATAS_BAWAH
            if bola.vy > 0:
                bola.vy = -bola.vy * 0.96
                suara_bola.play()

    for indeks, bola_pertama in enumerate(bola_bola):
        if not bola_pertama.aktif:
            continue
        for bola_kedua in bola_bola[indeks + 1:]:
            if not bola_kedua.aktif:
                continue
            dx = bola_kedua.x - bola_pertama.x
            dy = bola_kedua.y - bola_pertama.y
            jarak = math.hypot(dx, dy)
            if jarak >= DIAMETER_BOLA:
                continue

            if jarak == 0:
                normal_x, normal_y = 1, 0
            else:
                normal_x, normal_y = dx / jarak, dy / jarak

            tumpang_tindih = DIAMETER_BOLA - jarak
            bola_pertama.x -= normal_x * tumpang_tindih / 2
            bola_pertama.y -= normal_y * tumpang_tindih / 2
            bola_kedua.x += normal_x * tumpang_tindih / 2
            bola_kedua.y += normal_y * tumpang_tindih / 2

            kecepatan_rel = (
                (bola_kedua.vx - bola_pertama.vx) * normal_x
                + (bola_kedua.vy - bola_pertama.vy) * normal_y
            )
            if kecepatan_rel < 0:
                impuls = -(1 + 0.99) * kecepatan_rel / 2
                bola_pertama.vx -= impuls * normal_x
                bola_pertama.vy -= impuls * normal_y
                bola_kedua.vx += impuls * normal_x
                bola_kedua.vy += impuls * normal_y
                suara_bola.play()

    redaman = math.exp(-0.9 * dt)
    for bola in bola_bola:
        bola.vx *= redaman
        bola.vy *= redaman
        if math.hypot(bola.vx, bola.vy) < 8:
            bola.vx = 0
            bola.vy = 0


def perbarui_bola(bola_bola, dt, suara_bola):
    dt = min(dt, 0.04)
    kecepatan_maks = max(
        (math.hypot(bola.vx, bola.vy) for bola in bola_bola),
        default=0,
    )
    jumlah_substep = max(
        1,
        math.ceil(kecepatan_maks * dt / (RADIUS_BOLA / 2)),
    )
    dt_substep = dt / jumlah_substep
    for _ in range(jumlah_substep):
        perbarui_substep(bola_bola, dt_substep, suara_bola)


def main():
    pygame.mixer.pre_init(22050, -16, 1, 512)
    pygame.init()
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    suara_bola = muat_suara("suara_bola", "bola")
    suara_tongkat = muat_suara("suara_tongkat", "tongkat")

    layar = pygame.display.set_mode((LEBAR, TINGGI))
    pygame.display.set_caption("Simulasi Biliar")
    font_judul = pygame.font.Font(None, 36)
    font_petunjuk = pygame.font.Font(None, 24)
    clock = pygame.time.Clock()

    bola_bola = [
        Bola(170, 295, PUTIH, "putih"),
        Bola(800, 295, EMAS, "emas"),
        Bola(842, 271, BIRU, "biru"),
        Bola(842, 319, KUNING, "kuning"),
    ]
    bola_putih = bola_bola[0]
    arah_x, arah_y = 1, 0
    sedang_mengarahkan = False
    posisi_tarik = (bola_putih.x - 100, bola_putih.y)
    berjalan = True

    while berjalan:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                berjalan = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                jarak_ke_putih = math.hypot(
                    event.pos[0] - bola_putih.x,
                    event.pos[1] - bola_putih.y,
                )
                if semua_bola_berhenti(bola_bola) and jarak_ke_putih <= RADIUS_BOLA + 14:
                    sedang_mengarahkan = True
                    posisi_tarik = event.pos
            elif event.type == pygame.MOUSEMOTION and sedang_mengarahkan:
                posisi_tarik = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and sedang_mengarahkan:
                posisi_tarik = event.pos
                dx = bola_putih.x - posisi_tarik[0]
                dy = bola_putih.y - posisi_tarik[1]
                jarak_tarik = math.hypot(dx, dy)
                if jarak_tarik >= 12:
                    arah_x, arah_y = dx / jarak_tarik, dy / jarak_tarik
                    kecepatan = min(
                        KECEPATAN_MAKS,
                        jarak_tarik * SENSITIVITAS_TARIK,
                    )
                    bola_putih.vx = arah_x * kecepatan
                    bola_putih.vy = arah_y * kecepatan
                    suara_tongkat.play()
                sedang_mengarahkan = False

        if sedang_mengarahkan:
            dx = bola_putih.x - posisi_tarik[0]
            dy = bola_putih.y - posisi_tarik[1]
            jarak = math.hypot(dx, dy)
            if jarak > 0:
                arah_x, arah_y = dx / jarak, dy / jarak

        perbarui_bola(bola_bola, dt, suara_bola)
        if not bola_putih.aktif and semua_bola_berhenti(bola_bola):
            bola_putih.aktif = True
            bola_putih.x = 170
            bola_putih.y = 295
        gambar_meja(layar, font_judul, font_petunjuk)
        for bola in bola_bola:
            gambar_bola(layar, bola)
        if semua_bola_berhenti(bola_bola):
            jarak_tarik = math.hypot(
                bola_putih.x - posisi_tarik[0],
                bola_putih.y - posisi_tarik[1],
            ) if sedang_mengarahkan else 0
            gambar_tongkat(layar, bola_putih, arah_x, arah_y, jarak_tarik)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
