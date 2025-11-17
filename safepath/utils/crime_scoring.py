# safepath/utils/crime_scoring.py
import pandas as pd
from .geometry_utils import haversine
from .deepseek_client import rate_segment_risk

def summarize_crime_for_segment(a, b, crime_df, radius=200):
    """Count crimes near this road segment."""
    lat1, lon1 = a
    lat2, lon2 = b

    mid = ((lat1 + lat2)/2, (lon1 + lon2)/2)

    subset = crime_df[
        crime_df.apply(lambda row:
            haversine(mid[0], mid[1], row["latitude"], row["longitude"]) < radius,
            axis=1
        )
    ]

    summary = {
        "crime_count": len(subset),
        "most_common": subset["type"].value_counts().to_dict()
            if "type" in subset else {}
    }

    risk = rate_segment_risk(summary)
    return risk

