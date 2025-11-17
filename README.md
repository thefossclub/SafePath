# SafePath

**SafePath** is an intelligent navigation platform helps users choose **safer routes** instead of just fater ones. It analyzes real-time crime data, user reports, and police APIs to compute a dynamic Safety Index Score for every road segment while guiding people through the safest possible paths in urban areas.

## Technical Architecture

- **Frontend**: Tailwind CSS + Leaflet.js (OpenStreetMap)
- **Backend**: Django (core server), FastAPI (supporting microservices)
- **Database**: PostgreSQL + PostGIS for geospatial processing

## How It Works

- **Collect Data**: Crime stats, police API inputs, user-reported incidents.
- **Process Geo-Data**: Normalize, geocode, and store using PostGIS.
- **Compute Safety Index**: Weighted scoring based on crime history, density, and time-of-day.
- **Generate Routes**: Modified Dijkstra/A* algorithm prioritizing safety over shortest path.
- **Visualize**: Heatmaps + route overlays displayed using Leaflet.js.

## Installation & Setup
1. Clone the repository 
```
git clone https://github.com/LilSuperUser/SafePath.git
cd ./SafePath
```

2. Install the dependencies in a python virtual environment 
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Start the server 
```
python manage.py runserver
```

4. Visit 127.0.0.1:8000 <br>


## License

This project is licensed under the GPL v3 License. You are free to use, modify, and distribute this software under the terms of the [GPL v3 license](./LICENSE)
