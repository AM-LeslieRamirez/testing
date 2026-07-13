#!/usr/bin/env python3
import json, os, sys

TS = "2026-07-13T16:30:00Z"
TODAY = "2026-07-13"

# Exchange rates (July 2026 approx)
USD_MXN = 17.6
EUR_MXN = 19.5

def u(usd): return round(usd * USD_MXN)
def e(eur): return round(eur * EUR_MXN)

entries = [
  # ─── E1 IDA MX→EU ───────────────────────────────────────────────────────────
  {
    "timestamp": TS, "rutina": "B", "escenario": "E1", "tipo": "IDA",
    "origen": "MEX", "destino": "CDG",
    "fecha_ida": "2026-08-12", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Air France",
    "escalas": [],
    "precio_total_mxn": u(344), "precio_eur": None,
    "duracion": "~11h directo",
    "fuente": "Skyscanner",
    "verificado": False,
    "link": "https://www.skyscanner.com.mx/transporte/vuelos/mex/cdg/260812/"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E1", "tipo": "IDA",
    "origen": "MEX", "destino": "CDG",
    "fecha_ida": "2026-08-08", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Aeromexico / Air France",
    "escalas": [],
    "precio_total_mxn": u(441), "precio_eur": None,
    "duracion": "~11h directo",
    "fuente": "KAYAK",
    "verificado": False,
    "link": "https://www.kayak.com.mx/vuelos/MEX-CDG/2026-08-08"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E1", "tipo": "IDA",
    "origen": "MEX", "destino": "AMS",
    "fecha_ida": "2026-08-15", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "KLM",
    "escalas": [],
    "precio_total_mxn": u(365), "precio_eur": None,
    "duracion": "~12h directo",
    "fuente": "KAYAK",
    "verificado": False,
    "link": "https://www.kayak.com.mx/vuelos/MEX-AMS/2026-08-15"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E1", "tipo": "IDA",
    "origen": "MEX", "destino": "AMS",
    "fecha_ida": "2026-08-08", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "KLM",
    "escalas": [],
    "precio_total_mxn": u(390), "precio_eur": None,
    "duracion": "~12h directo",
    "fuente": "KAYAK",
    "verificado": False,
    "link": "https://www.kayak.com.mx/vuelos/MEX-AMS/2026-08-08"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E1", "tipo": "IDA",
    "origen": "MEX", "destino": "FCO",
    "fecha_ida": "2026-08-09", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "ITA Airways / Aeromexico",
    "escalas": ["MAD"],
    "precio_total_mxn": u(434), "precio_eur": None,
    "duracion": "~15h con escala MAD",
    "fuente": "KAYAK",
    "verificado": False,
    "link": "https://www.kayak.com.mx/vuelos/MEX-FCO/2026-08-09"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E1", "tipo": "IDA",
    "origen": "MEX", "destino": "LHR",
    "fecha_ida": "2026-08-08", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Iberia",
    "escalas": ["MAD"],
    "precio_total_mxn": u(438), "precio_eur": None,
    "duracion": "~14h con escala MAD",
    "fuente": "KAYAK",
    "verificado": False,
    "link": "https://www.kayak.com.mx/vuelos/MEX-LHR/2026-08-08"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E1", "tipo": "IDA",
    "origen": "MEX", "destino": "LHR",
    "fecha_ida": "2026-08-14", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Iberia",
    "escalas": ["MAD"],
    "precio_total_mxn": u(410), "precio_eur": None,
    "duracion": "~14h con escala MAD",
    "fuente": "KAYAK / Expedia",
    "verificado": False,
    "link": "https://www.kayak.com.mx/vuelos/MEX-LHR/2026-08-14"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E1", "tipo": "IDA",
    "origen": "CUN", "destino": "MAD",
    "fecha_ida": "2026-08-14", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Iberia",
    "escalas": [],
    "precio_total_mxn": u(314), "precio_eur": None,
    "duracion": "~10h directo",
    "fuente": "Skyscanner",
    "verificado": False,
    "link": "https://www.skyscanner.com.mx/transporte/vuelos/cun/mad/260814/"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E1", "tipo": "IDA",
    "origen": "NLU", "destino": "MAD",
    "fecha_ida": "2026-08-11", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Aeromexico",
    "escalas": ["MEX"],
    "precio_total_mxn": u(348), "precio_eur": None,
    "duracion": "~13h con escala MEX",
    "fuente": "Skyscanner (MEXA→MAD)",
    "verificado": False,
    "link": "https://www.skyscanner.com.mx/transporte/vuelos/nlu/mad/260811/"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E1", "tipo": "IDA",
    "origen": "QRO", "destino": "MAD",
    "fecha_ida": "2026-08-09", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Aeromexico / Iberojet",
    "escalas": ["MEX"],
    "precio_total_mxn": u(363), "precio_eur": None,
    "duracion": "~13h con escala MEX",
    "fuente": "Skyscanner",
    "verificado": False,
    "link": "https://www.espanol.skyscanner.com/rutas/qro/mad/queretaro-a-madrid-barajas.html"
  },
  # ─── E2 VUELTA EU→MX ────────────────────────────────────────────────────────
  {
    "timestamp": TS, "rutina": "B", "escenario": "E2", "tipo": "VUELTA",
    "origen": "MAD", "destino": "MEX",
    "fecha_ida": "2026-08-25", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Iberia",
    "escalas": [],
    "precio_total_mxn": u(467), "precio_eur": None,
    "duracion": "~12h directo",
    "fuente": "KAYAK",
    "verificado": False,
    "link": "https://www.kayak.com.mx/vuelos/MAD-MEX/2026-08-25"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E2", "tipo": "VUELTA",
    "origen": "MAD", "destino": "MEX",
    "fecha_ida": "2026-09-03", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Aeromexico",
    "escalas": [],
    "precio_total_mxn": u(450), "precio_eur": None,
    "duracion": "~12h directo",
    "fuente": "KAYAK / Expedia",
    "verificado": False,
    "link": "https://www.kayak.com.mx/vuelos/MAD-MEX/2026-09-03"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E2", "tipo": "VUELTA",
    "origen": "AMS", "destino": "MEX",
    "fecha_ida": "2026-09-05", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "KLM",
    "escalas": [],
    "precio_total_mxn": u(502), "precio_eur": None,
    "duracion": "~13h directo",
    "fuente": "KAYAK",
    "verificado": False,
    "link": "https://www.kayak.com.mx/vuelos/AMS-MEX/2026-09-05"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E2", "tipo": "VUELTA",
    "origen": "CDG", "destino": "MEX",
    "fecha_ida": "2026-09-07", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Air France",
    "escalas": [],
    "precio_total_mxn": u(480), "precio_eur": None,
    "duracion": "~11h directo",
    "fuente": "Expedia / Skyscanner",
    "verificado": False,
    "link": "https://www.kayak.com.mx/vuelos/CDG-MEX/2026-09-07"
  },
  # ─── E3 RT MX↔EU escala MAD ─────────────────────────────────────────────────
  {
    "timestamp": TS, "rutina": "B", "escenario": "E3", "tipo": "RT",
    "origen": "MEX", "destino": "MAD",
    "fecha_ida": "2026-08-08", "fecha_vuelta": "2026-08-27", "dias_estancia": 19,
    "aerolinea": "Aeromexico",
    "escalas": [],
    "precio_total_mxn": u(515), "precio_eur": None,
    "duracion": "~10h30 directo c/tramo",
    "fuente": "momondo / Kayak (mejor deal disponible)",
    "verificado": False,
    "link": "https://www.kayak.com.mx/vuelos/MEX-MAD/2026-08-08/MAD-MEX/2026-08-27"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E3", "tipo": "RT",
    "origen": "MEX", "destino": "MAD",
    "fecha_ida": "2026-08-12", "fecha_vuelta": "2026-08-31", "dias_estancia": 19,
    "aerolinea": "Aeromexico / Iberia",
    "escalas": [],
    "precio_total_mxn": u(696), "precio_eur": None,
    "duracion": "~10h30 directo c/tramo",
    "fuente": "momondo",
    "verificado": False,
    "link": "https://www.kayak.com.mx/vuelos/MEX-MAD/2026-08-12/MAD-MEX/2026-08-31"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E3", "tipo": "RT",
    "origen": "CUN", "destino": "MAD",
    "fecha_ida": "2026-08-15", "fecha_vuelta": "2026-09-03", "dias_estancia": 19,
    "aerolinea": "Iberia",
    "escalas": [],
    "precio_total_mxn": u(610), "precio_eur": None,
    "duracion": "~10h directo c/tramo",
    "fuente": "Skyscanner (estimado RT bundled)",
    "verificado": False,
    "link": "https://www.skyscanner.com.mx/transporte/vuelos/cun/mad/260815/mad/cun/260903/"
  },
  # ─── E4 TRAMO EU→BKK ────────────────────────────────────────────────────────
  {
    "timestamp": TS, "rutina": "B", "escenario": "E4", "tipo": "TRAMO",
    "origen": "MAD", "destino": "BKK",
    "fecha_ida": "2026-08-20", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Turkish Airlines",
    "escalas": ["IST"],
    "precio_total_mxn": e(275), "precio_eur": 275,
    "duracion": "~14h vía IST",
    "fuente": "Jetcost / eDreams",
    "verificado": False,
    "link": "https://www.skyscanner.es/transporte/vuelos/mad/bkk/260820/"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E4", "tipo": "TRAMO",
    "origen": "MAD", "destino": "BKK",
    "fecha_ida": "2026-08-15", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Emirates",
    "escalas": ["DXB"],
    "precio_total_mxn": e(283), "precio_eur": 283,
    "duracion": "~16h vía DXB",
    "fuente": "eDreams",
    "verificado": False,
    "link": "https://www.skyscanner.es/transporte/vuelos/mad/bkk/260815/"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E4", "tipo": "TRAMO",
    "origen": "BCN", "destino": "BKK",
    "fecha_ida": "2026-08-20", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Qatar Airways",
    "escalas": ["DOH"],
    "precio_total_mxn": e(332), "precio_eur": 332,
    "duracion": "~16h vía DOH",
    "fuente": "KAYAK / Expedia",
    "verificado": False,
    "link": "https://www.skyscanner.es/transporte/vuelos/bcn/bkk/260820/"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E4", "tipo": "TRAMO",
    "origen": "CDG", "destino": "BKK",
    "fecha_ida": "2026-08-18", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "Air France",
    "escalas": [],
    "precio_total_mxn": e(284), "precio_eur": 284,
    "duracion": "~11h directo",
    "fuente": "Skyscanner",
    "verificado": False,
    "link": "https://www.skyscanner.es/transporte/vuelos/cdg/bkk/260818/"
  },
  # ─── E6 TREN MAD→otra EU ────────────────────────────────────────────────────
  {
    "timestamp": TS, "rutina": "B", "escenario": "E6", "tipo": "TREN",
    "origen": "MAD", "destino": "BCN",
    "fecha_ida": "2026-08-15", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "tren Renfe Avlo",
    "escalas": [],
    "precio_total_mxn": e(7), "precio_eur": 7,
    "duracion": "2h30",
    "fuente": "Renfe / Omio",
    "verificado": False,
    "link": "https://www.renfe.com/es/en/travel/prepare-your-trip/billetes-ave-y-largadistancia/all-tickets"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E6", "tipo": "TREN",
    "origen": "MAD", "destino": "BCN",
    "fecha_ida": "2026-08-15", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "tren Renfe AVE",
    "escalas": [],
    "precio_total_mxn": e(38), "precio_eur": 38,
    "duracion": "2h30",
    "fuente": "Renfe / Rail Europe (30d adelanto)",
    "verificado": False,
    "link": "https://www.renfe.com/es/en/viajeros/viajes-y-servicios/ave-y-larga-distancia"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E6", "tipo": "TREN",
    "origen": "MAD", "destino": "BCN",
    "fecha_ida": "2026-08-20", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "tren Renfe AVE Turista",
    "escalas": [],
    "precio_total_mxn": e(94), "precio_eur": 94,
    "duracion": "2h30",
    "fuente": "Renfe (tarifa turista estándar)",
    "verificado": False,
    "link": "https://www.renfe.com/es/en/viajeros/viajes-y-servicios/ave-y-larga-distancia"
  },
  {
    "timestamp": TS, "rutina": "B", "escenario": "E6", "tipo": "TREN",
    "origen": "MAD", "destino": "CDG",
    "fecha_ida": "2026-08-15", "fecha_vuelta": None, "dias_estancia": None,
    "aerolinea": "tren Renfe AVE + TGV INOUI",
    "escalas": ["BCN"],
    "precio_total_mxn": e(68), "precio_eur": 68,
    "duracion": "~9h15 (MAD-BCN 2h30 + BCN-PAR 6h42)",
    "fuente": "Renfe + SNCF Connect / Omio",
    "verificado": False,
    "link": "https://www.sncf-connect.com/en-en/train/route/barcelona/paris"
  },
]

fn = f"prices/{TODAY}.json"
data = json.load(open(fn)) if os.path.exists(fn) else []
data.extend(entries)
json.dump(data, open(fn, 'w'), indent=2, ensure_ascii=False)
print(f"Appended {len(entries)} entries → total {len(data)} in {fn}")

# Print urgency summary
urgent = []
normal_deals = []
thresholds = {
    "E1_MAD":  {"normal": 6500,  "urgent": 5200},
    "E1_EU":   {"normal": 7500,  "urgent": 6000},
    "E2":      {"normal": 7000,  "urgent": 5600},
    "E3_MAD":  {"normal": 13000, "urgent": 10400},
    "E3_EU":   {"normal": 15000, "urgent": 12000},
    "E4_eur":  {"normal": 280,   "urgent": 220},
    "E6_eur":  {"normal": 150,   "urgent": 100},
}

for e in entries:
    sc = e["escenario"]
    dest = e["destino"]
    mxn = e["precio_total_mxn"]
    eur = e.get("precio_eur")

    if sc == "E1":
        t = thresholds["E1_MAD"] if dest == "MAD" else thresholds["E1_EU"]
        if mxn <= t["urgent"]:
            urgent.append(f"URGENT E1 {e['origen']}→{dest} {mxn:,} MXN")
        elif mxn <= t["normal"]:
            normal_deals.append(f"DEAL E1 {e['origen']}→{dest} {mxn:,} MXN")
    elif sc == "E2":
        t = thresholds["E2"]
        if mxn <= t["urgent"]:
            urgent.append(f"URGENT E2 {e['origen']}→{dest} {mxn:,} MXN")
        elif mxn <= t["normal"]:
            normal_deals.append(f"DEAL E2 {e['origen']}→{dest} {mxn:,} MXN")
    elif sc == "E3":
        t = thresholds["E3_MAD"] if dest == "MAD" else thresholds["E3_EU"]
        if mxn <= t["urgent"]:
            urgent.append(f"URGENT E3 {e['origen']}↔{dest} {mxn:,} MXN RT")
        elif mxn <= t["normal"]:
            normal_deals.append(f"DEAL E3 {e['origen']}↔{dest} {mxn:,} MXN RT")
    elif sc == "E4" and eur:
        t = thresholds["E4_eur"]
        if eur <= t["urgent"]:
            urgent.append(f"URGENT E4 {e['origen']}→{dest} €{eur}")
        elif eur <= t["normal"]:
            normal_deals.append(f"DEAL E4 {e['origen']}→{dest} €{eur}")
    elif sc == "E6" and eur:
        t = thresholds["E6_eur"]
        if eur <= t["urgent"]:
            urgent.append(f"URGENT E6 {e['origen']}→{dest} €{eur} ({e['aerolinea']})")
        elif eur <= t["normal"]:
            normal_deals.append(f"DEAL E6 {e['origen']}→{dest} €{eur} ({e['aerolinea']})")

print("\n=== URGENT ===")
for x in urgent: print(" ", x)
print("\n=== NORMAL DEALS ===")
for x in normal_deals: print(" ", x)
print(f"\nTotal urgent: {len(urgent)}, Total deals: {len(normal_deals)}")
