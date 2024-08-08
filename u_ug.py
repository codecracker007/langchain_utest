import pymongo

# Connect to MongoDB (default URI for local instance)


c = pymongo.MongoClient("mongodb+srv://chandrakasturi:Bisleri1234@cluster0.ehbe5dz.mongodb.net/",server_api=pymongo.server_api.ServerApi('1'))

# Select the database and collection
db = c['sahasra_subjectdata']  # Replace 'your_database_name' with your database name
collection = db['topic_subtopic']  # Replace 'your_collection_name' with your collection name

# Data to be inserted
data = {
  "Details": [
    {
      "Subject": "Physics",
      "Topic": "Electricity",
      "Sub Topic": "Ohm’s Law"
    },
    {
      "Subject": "Physics",
      "Topic": "Magnetic Effects of Electric Current",
      "Sub Topic": "Electromagnetic induction"
    },
    {
      "Subject": "Physics",
      "Topic": "Velocity",
      "Sub Topic": "Acceleration"
    },
    {
      "Subject": "Biology",
      "Topic": "How do organisms reproduce",
      "Sub Topic": "Sexual reproduction in animals"
    },
    {
      "Subject": "Biology",
      "Topic": "Life processes",
      "Sub Topic": "Respiration in humans"
    },
    {
      "Subject": "Biology",
      "Topic": "Our environment",
      "Sub Topic": "Food chains and food webs"
    },
    {
      "Subject": "English",
      "Topic": "A Shady Plot",
      "Sub Topic": "John Hallock"
    },
    {
      "Subject": "English",
      "Topic": "Julius Caesar",
      "Sub Topic": "Brutus"
    },
    {
      "Subject": "English",
      "Topic": "Ozymandias"
    },
    {
      "Subject": "History",
      "Topic": "The Age of Industrialization",
      "Sub Topic": "Hand Labour and Steam Power:"
    },
    {
      "Subject": "History",
      "Topic": "The Rise of Nationalism in Europe",
      "Sub Topic": "The Age of Revolutions: 1830-1848"
    },
    {
      "Subject": "History",
      "Topic": "Work, Life and Leisure",
      "Sub Topic": "Characteristics of the City:"
    }
  ]
}

# Extract individual documents from the 'Details' array
documents = data["Details"]

# Insert each document into the collection
result = collection.insert_many(documents)

# Print the inserted_ids to confirm insertion
print(f'Documents inserted with record ids {result.inserted_ids}')
