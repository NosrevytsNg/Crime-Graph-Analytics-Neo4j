{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "ff480b91-7ed6-4ed8-9064-270feb562be0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CSV has been created successfully\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = 'D:\\\\Study Materials\\\\Murdoch\\\\TJA 2025\\\\ICT203 Artificial Intelligence and Intelligent Agents\\\\Assignment 2\\\\crime_subset.csv'\n",
    "crime_data = pd.read_csv(file_path)\n",
    "\n",
    "\n",
    "# Convert 'date' to datetime and extract year and month\n",
    "crime_data['date'] = pd.to_datetime(crime_data['date'], format='%m/%d/%y', errors='coerce')\n",
    "crime_data['year'] = crime_data['date'].dt.year\n",
    "crime_data['month'] = crime_data['date'].dt.month\n",
    "\n",
    "# Link unique crime ID to crime from the 'number' column\n",
    "crime_data['crime_id'] = crime_data['number'].astype(str)\n",
    "\n",
    "# Crime Node\n",
    "crime_node = crime_data[['crime_id', 'crime', 'date', 'year', 'month']].drop_duplicates()\n",
    "\n",
    "# Neighborhood Node\n",
    "\n",
    "neighborhood_columns = ['neighborhood', 'location', 'road', 'city', 'county', 'state', 'postcode']\n",
    "neighborhood_node = crime_data[neighborhood_columns].drop_duplicates(subset=['neighborhood'])\n",
    "\n",
    "# Beat Node\n",
    "beat_columns = ['beat', 'npu']\n",
    "beat_node = crime_data[beats_columns].drop_duplicates(subset=['beat'])\n",
    "\n",
    "# Property Node\n",
    "property_types = crime_data['type'].dropna().unique()\n",
    "property_type_node = pd.DataFrame({'property_type': property_types})\n",
    "\n",
    "\n",
    "# Relationships DataFrames\n",
    "occurred_in = crime_data[['crime_id', 'neighborhood']].dropna().drop_duplicates()\n",
    "on_beat = crime_data[['crime_id', 'beat']].dropna().drop_duplicates()\n",
    "involved_in = crime_data[['crime_id', 'type']].rename(columns={'type': 'property_type'}).dropna().drop_duplicates()\n",
    "\n",
    "#Output Directory (od)\n",
    "od = 'D:\\\\Study Materials\\\\Murdoch\\\\TJA 2025\\\\ICT203 Artificial Intelligence and Intelligent Agents\\\\Assignment 2'\n",
    "\n",
    "# Save to CSV\n",
    "crime_node.to_csv(od + '\\\\crime_node.csv', index=False)\n",
    "neighborhood_node.to_csv(od + '\\\\neighborhood_node.csv', index=False)\n",
    "beat_node.to_csv(od + '\\\\beat_node.csv', index=False)\n",
    "property_type_node.to_csv(od + '\\\\property_type_nodes.csv', index=False)\n",
    "occurred_in.to_csv(od + '\\\\occurred_in.csv', index=False)\n",
    "on_beat.to_csv(od + '\\\\on_beat.csv', index=False)\n",
    "involved_in.to_csv(od + '\\\\involved_in.csv', index=False)\n",
    "\n",
    "print(\"CSV has been created successfully\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54da4b0d-a5aa-49b6-b30a-5ed41c59de0a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
