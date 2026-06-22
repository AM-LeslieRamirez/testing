# Monitor de vuelos MX → MAD → BKK

Estado compartido del sistema multi-rutina que caza vuelos para Leslie.

## Estructura

```
.
├── README.md                  # Este archivo
├── config/
│   └── thresholds.json        # Thresholds por escenario (editar aquí cambia el comportamiento)
├── baseline.json              # Promedios rolling 7 días (actualiza Rutina D los lunes)
├── deals_history.json         # Timeline de deals detectados
└── prices/
    └── YYYY-MM-DD.json        # 1 archivo por día con todas las entradas de A/B/C
```

## Rutinas que escriben aquí

- **A — Hot Date** (cada 3h, 8/día): foco fecha objetivo 4-5 ago + redondo MX↔BKK combinado.
- **B — Wide Mexico** (cada 8h, 3/día): cobertura amplia 5 aeropuertos × 4 escenarios.
- **C — Madrugada España** (1/día, 7 PM CDMX = 3 AM CET): snapshot Iberojet/Iberia/Air Europa/Plus Ultra.
- **D — Consolidator** (1/día, 5 PM CDMX): lee todo, calcula deltas, crea draft maestro en Gmail.

## Aeropuertos monitoreados

| Código | Ciudad | Aerolíneas directas a MAD |
|---|---|---|
| MEX | CDMX Benito Juárez | Aeromexico, Iberia, Air Europa, Plus Ultra, Iberojet, Wamos Air, World2Fly |
| NLU | CDMX Felipe Ángeles | Aeromexico |
| CUN | Cancún | Iberojet, Air Europa, World2Fly, Aeromexico, Wamos Air |
| QRO | Querétaro | Iberojet (mié + sáb) |
| MID | Mérida | Plus Ultra (canal nuevo 2026) |

## Schema de `prices/YYYY-MM-DD.json`

Array append-only, cada rutina añade entradas al final:

```json
[
  {
    "timestamp": "2026-08-04T14:05:00Z",
    "rutina": "A",
    "escenario": "P",
    "origen_mx": "CUN",
    "destino": "BKK",
    "via": "MAD",
    "fecha_ida": "2026-08-05",
    "fecha_vuelta": "2026-08-22",
    "aerolinea": "World2Fly+Iberojet",
    "precio_total_mxn": 16500,
    "fuente": "skyscanner_snippet",
    "verificado": false,
    "link": "https://..."
  }
]
```

## Schema de `config/thresholds.json`

Editable sin tocar prompts:

- `threshold_mxn` / `threshold_eur`: precio bajo el cual se considera "deal".
- `urgent_mxn` / `urgent_eur`: precio bajo el cual se considera "URGENT" (>20% bajo threshold) — dispara draft inmediato.

## Plan del viaje

- Salida ideal: **4-5 ago 2026** desde cualquier aeropuerto MX.
- Estancia España: ~17 días.
- Vuelta ideal: **18-26 ago 2026** (si encuentra ganga; el plan principal es solo ida).
- Destino final: Bangkok (BKK), preferiblemente con stopover en Madrid.
- REGLA DURA: prohibido escalas en EE.UU. (requieren visa/ESTA).
