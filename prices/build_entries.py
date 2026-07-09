#!/usr/bin/env python3
import json, sys, os

TS = "2026-07-09T02:02:19Z"

entries = [
  # ── E5 COMBO_IDA ──────────────────────────────────────────────────────────
  # 1. CUN→MAD (Air Europa, Tue 4-Aug) + MAD→BKK (Iberojet direct, Sun 9-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "CUN", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-04", "fecha_vuelta": None,
    "aerolineas": ["Air Europa", "Iberojet"],
    "escalas": ["MAD"],
    "precio_total_mxn": 11253,
    "precio_desglose_mxn": {"MX_EU": 5795, "EU_BKK": 5458},
    "fuente": "WebSearch: Expedia CUN-MAD Air Europa $305 USD; Iberojet MAD-BKK €295 (sep ref €295.72)",
    "verificado": False,
    "link": "https://www.aireuropa.com/en-us/flight-deals-from-cancun"
  },
  # 2. CUN→MAD (Air Europa, Sun 9-Aug) + MAD→BKK (Iberojet, Thu 13-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "CUN", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-09", "fecha_vuelta": None,
    "aerolineas": ["Air Europa", "Iberojet"],
    "escalas": ["MAD"],
    "precio_total_mxn": 11253,
    "precio_desglose_mxn": {"MX_EU": 5795, "EU_BKK": 5458},
    "fuente": "WebSearch: Expedia CUN-MAD Air Europa $305 USD; Iberojet MAD-BKK €295",
    "verificado": False,
    "link": "https://www.aireuropa.com/en-us/flight-deals-from-cancun"
  },
  # 3. CUN→MAD (Iberojet, Fri 7-Aug) + MAD→BKK (Iberojet direct, Thu 13-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "CUN", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-07", "fecha_vuelta": None,
    "aerolineas": ["Iberojet", "Iberojet"],
    "escalas": ["MAD"],
    "precio_total_mxn": 12581,
    "precio_desglose_mxn": {"MX_EU": 7123, "EU_BKK": 5458},
    "fuente": "WebSearch: eDreams Iberojet CUN-MAD €385 Aug pico; Iberojet MAD-BKK €295",
    "verificado": False,
    "link": "https://www.iberojet.com/en/flights-from-cancun-to-madrid"
  },
  # 4. CUN→MAD (Air Europa, Tue 4-Aug) + MAD→BKK via Turkish IST (Sun 9-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "CUN", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-04", "fecha_vuelta": None,
    "aerolineas": ["Air Europa", "Turkish Airlines"],
    "escalas": ["MAD", "IST"],
    "precio_total_mxn": 12065,
    "precio_desglose_mxn": {"MX_EU": 5795, "EU_BKK": 6270},
    "fuente": "WebSearch: AirEuropa CUN-MAD $305; Turkish MAD-IST-BKK ~$330 USD est",
    "verificado": False,
    "link": "https://www.turkishairlines.com/en/flights-from-istanbul-to-bangkok"
  },
  # 5. CUN→MAD (Air Europa, Tue 4-Aug) + MAD→BKK via Etihad AUH (Sat 8-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "CUN", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-04", "fecha_vuelta": None,
    "aerolineas": ["Air Europa", "Etihad Airways"],
    "escalas": ["MAD", "AUH"],
    "precio_total_mxn": 11875,
    "precio_desglose_mxn": {"MX_EU": 5795, "EU_BKK": 6080},
    "fuente": "WebSearch: AirEuropa CUN-MAD $305; Etihad MAD-AUH-BKK ~$320 USD est (AUH-BKK base $147)",
    "verificado": False,
    "link": "https://www.etihad.com/en/flights/flights-from-abu-dhabi-to-bangkok"
  },
  # 6. CUN→MAD (Air Europa, Tue 4-Aug) + MAD→BKK via Qatar DOH (Sun 9-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "CUN", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-04", "fecha_vuelta": None,
    "aerolineas": ["Air Europa", "Qatar Airways"],
    "escalas": ["MAD", "DOH"],
    "precio_total_mxn": 12350,
    "precio_desglose_mxn": {"MX_EU": 5795, "EU_BKK": 6555},
    "fuente": "WebSearch: AirEuropa CUN-MAD $305; Qatar MAD-DOH-BKK ~$345 USD est",
    "verificado": False,
    "link": "https://www.qatarairways.com/en/destinations/flights-to-bangkok.html"
  },
  # 7. CUN→MAD (World2Fly, Sat 8-Aug) + MAD→BKK (Iberojet direct, Sun 9-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "CUN", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-08", "fecha_vuelta": None,
    "aerolineas": ["World2Fly", "Iberojet"],
    "escalas": ["MAD"],
    "precio_total_mxn": 12110,
    "precio_desglose_mxn": {"MX_EU": 6650, "EU_BKK": 5460},
    "fuente": "WebSearch: World2Fly CUN-MAD ~$350 USD est; Iberojet MAD-BKK €295",
    "verificado": False,
    "link": "https://www.iberojet.com/en/flights-from-madrid-to-bangkok-airport"
  },
  # 8. CUN→MAD (Iberojet Mon 3-Aug) + MAD→BKK (Iberojet Thu 6-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "CUN", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-03", "fecha_vuelta": None,
    "aerolineas": ["Iberojet", "Iberojet"],
    "escalas": ["MAD"],
    "precio_total_mxn": 12488,
    "precio_desglose_mxn": {"MX_EU": 7123, "EU_BKK": 5365},
    "fuente": "WebSearch: Iberojet CUN-MAD €385; Iberojet MAD-BKK €290 Aug inicio",
    "verificado": False,
    "link": "https://vuelos.iberojet.com/en/flights-from-madrid-to-bangkok"
  },
  # 9. QRO→MAD (Iberojet Thu 6-Aug) + MAD→BKK (Iberojet Sun 9-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "QRO", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-06", "fecha_vuelta": None,
    "aerolineas": ["Iberojet", "Iberojet"],
    "escalas": ["MAD"],
    "precio_total_mxn": 12583,
    "precio_desglose_mxn": {"MX_EU": 7125, "EU_BKK": 5458},
    "fuente": "WebSearch: Skyscanner QRO-MAD $375; Iberojet MAD-BKK €295",
    "verificado": False,
    "link": "https://www.espanol.skyscanner.com/rutas/qro/mad/queretaro-a-madrid-barajas.html"
  },
  # 10. MEX→MAD (Aeromexico Wed 5-Aug) + MAD→BKK (Iberojet Sun 9-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "MEX", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-05", "fecha_vuelta": None,
    "aerolineas": ["Aeromexico", "Iberojet"],
    "escalas": ["MAD"],
    "precio_total_mxn": 14578,
    "precio_desglose_mxn": {"MX_EU": 9120, "EU_BKK": 5458},
    "fuente": "WebSearch: Expedia Aeromexico MEX-MAD $480 USD Aug; Iberojet MAD-BKK €295",
    "verificado": False,
    "link": "https://www.aeromexico.com/en_us/flights-from-mexico-city-to-madrid"
  },
  # 11. MEX→MAD (Iberia Wed 5-Aug) + MAD→BKK (Iberojet Sun 9-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "MEX", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-05", "fecha_vuelta": None,
    "aerolineas": ["Iberia", "Iberojet"],
    "escalas": ["MAD"],
    "precio_total_mxn": 14198,
    "precio_desglose_mxn": {"MX_EU": 8740, "EU_BKK": 5458},
    "fuente": "WebSearch: Expedia Iberia MEX-MAD $460 USD; Iberojet MAD-BKK €295",
    "verificado": False,
    "link": "https://www.iberia.com/us/cheap-flights/Mexico-City-Madrid/"
  },
  # 12. MEX→CDG (AF Wed 5-Aug) + CDG→BKK (AF Sat 8-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "MEX", "destino_eu": "CDG", "destino_final": "BKK",
    "fecha_ida": "2026-08-05", "fecha_vuelta": None,
    "aerolineas": ["Air France", "Air France"],
    "escalas": ["CDG"],
    "precio_total_mxn": 18335,
    "precio_desglose_mxn": {"MX_EU": 10070, "EU_BKK": 8265},
    "fuente": "WebSearch: MEX-CDG ~$530 USD est; Travelocity AF CDG-BKK $435; KAYAK CDG-BKK $387",
    "verificado": False,
    "link": "https://wwws.airfrance.us/en-us/flights-to-bangkok"
  },
  # 13. MEX→AMS (KLM Wed 5-Aug) + AMS→BKK (KLM Sat 8-Aug)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_IDA",
    "origen_mx": "MEX", "destino_eu": "AMS", "destino_final": "BKK",
    "fecha_ida": "2026-08-05", "fecha_vuelta": None,
    "aerolineas": ["KLM", "KLM"],
    "escalas": ["AMS"],
    "precio_total_mxn": 17100,
    "precio_desglose_mxn": {"MX_EU": 9690, "EU_BKK": 7410},
    "fuente": "WebSearch: MEX-AMS KLM ~$510 USD est; KAYAK AMS-BKK $393; Skyscanner $343",
    "verificado": False,
    "link": "https://www.klm.nl/en-nl/flights-from-amsterdam-to-bangkok"
  },
  # ── E5 COMBO_RT ──────────────────────────────────────────────────────────
  # 14. CUN↔MAD + MAD↔BKK full round (Air Europa + Iberojet) ~17d BKK stay
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_RT",
    "origen_mx": "CUN", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-04", "fecha_vuelta": "2026-08-25",
    "dias_estancia": 21,
    "aerolineas": ["Air Europa", "Iberojet", "Iberojet", "Air Europa"],
    "escalas": ["MAD"],
    "precio_total_mxn": 22598,
    "precio_desglose_mxn": {"MX_EU": 5795, "EU_BKK": 5458, "BKK_EU": 5550, "EU_MX": 5795},
    "fuente": "WebSearch: AirEuropa CUN-MAD $305; Iberojet MAD-BKK €295; Iberojet BKK-MAD ~€300 est; AirEuropa MAD-CUN $305",
    "verificado": False,
    "link": "https://www.iberojet.com/en/flights-from-madrid-to-bangkok"
  },
  # 15. CUN↔MAD + MAD↔BKK full round - option B Aug23 return
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_RT",
    "origen_mx": "CUN", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-04", "fecha_vuelta": "2026-08-25",
    "dias_estancia": 21,
    "aerolineas": ["Air Europa", "Iberojet", "Iberojet", "Iberojet"],
    "escalas": ["MAD"],
    "precio_total_mxn": 23431,
    "precio_desglose_mxn": {"MX_EU": 5795, "EU_BKK": 5458, "BKK_EU": 5058, "EU_MX": 7120},
    "fuente": "WebSearch: AirEuropa CUN-MAD $305; Iberojet MAD-BKK €295; Iberojet BKK-MAD €273; Iberojet MAD-CUN €385",
    "verificado": False,
    "link": "https://www.iberojet.com/en/flights-from-cancun-to-madrid"
  },
  # 16. QRO↔MAD + MAD↔BKK round trip via Iberojet
  {
    "timestamp": TS, "rutina": "A", "escenario": "E5", "tipo": "COMBO_RT",
    "origen_mx": "QRO", "destino_eu": "MAD", "destino_final": "BKK",
    "fecha_ida": "2026-08-06", "fecha_vuelta": "2026-08-26",
    "dias_estancia": 20,
    "aerolineas": ["Iberojet", "Iberojet", "Iberojet", "Iberojet"],
    "escalas": ["MAD"],
    "precio_total_mxn": 25808,
    "precio_desglose_mxn": {"MX_EU": 7125, "EU_BKK": 5458, "BKK_EU": 6100, "EU_MX": 7125},
    "fuente": "WebSearch: Iberojet QRO-MAD $375; Iberojet MAD-BKK €295; Iberojet BKK-MAD ~€330 est; Iberojet MAD-QRO $375",
    "verificado": False,
    "link": "https://www.espanol.skyscanner.com/rutas/qro/mad/queretaro-a-madrid-barajas.html"
  },
  # ── E1 IDA sola MX→EU (precios bajos) ──────────────────────────────────
  # 17. CUN→MAD Air Europa (below threshold 6500 MXN)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E1", "tipo": "IDA",
    "origen_mx": "CUN", "destino_eu": "MAD",
    "fecha_ida": "2026-08-04", "fecha_vuelta": None,
    "aerolineas": ["Air Europa"],
    "escalas": [],
    "precio_total_mxn": 5795,
    "fuente": "WebSearch: Expedia CUN-MAD one-way $305 USD (base from $199, Aug est)",
    "verificado": False,
    "link": "https://www.aireuropa.com/en-us/flight-deals-from-cancun"
  },
  # 18. CUN→MAD Air Europa (Sunday Sep window)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E1", "tipo": "IDA",
    "origen_mx": "CUN", "destino_eu": "MAD",
    "fecha_ida": "2026-08-02", "fecha_vuelta": None,
    "aerolineas": ["Air Europa"],
    "escalas": [],
    "precio_total_mxn": 5795,
    "fuente": "WebSearch: Expedia CUN-MAD one-way $305 USD Air Europa Sun flight",
    "verificado": False,
    "link": "https://www.aireuropa.com/en-us/flight-deals-from-cancun"
  },
  # ── E3 RT MX↔EU (precio interesante) ────────────────────────────────────
  # 19. CUN↔MAD RT Air Europa (below threshold 13000 MXN for MAD)
  {
    "timestamp": TS, "rutina": "A", "escenario": "E3", "tipo": "RT",
    "origen_mx": "CUN", "destino_eu": "MAD",
    "fecha_ida": "2026-08-04", "fecha_vuelta": "2026-08-25",
    "dias_estancia": 21,
    "aerolineas": ["Air Europa"],
    "escalas": [],
    "precio_total_mxn": 11590,
    "fuente": "WebSearch: AirEuropa CUN-MAD $305 x2 RT; Skyscanner MAD-CUN £258 ≈ $305",
    "verificado": False,
    "link": "https://www.aireuropa.com/en-us/flight-deals-from-cancun"
  }
]

# Append to prices/$TODAY.json
fn = f"prices/2026-07-09.json"
if os.path.exists(fn):
    existing = json.load(open(fn))
else:
    existing = []
existing.extend(entries)
with open(fn, "w") as f:
    json.dump(existing, f, indent=2, ensure_ascii=False)

print(f"Appended {len(entries)} entries to {fn}")
print(f"Total entries in file: {len(existing)}")

# Summary by scenario/tipo
from collections import Counter
counts = Counter((e.get('escenario','?'), e.get('tipo','?')) for e in entries)
for k,v in sorted(counts.items()):
    print(f"  {k[0]} {k[1]}: {v}")
