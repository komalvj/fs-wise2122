import data
import datastore as ds

# public DataStore objects
tds = ds.PlacesDataStore()

# DataFactory object instantiation without reference, invoke chainable functions
ds.DataFactory(tds) \
      .import_places(data.places)

