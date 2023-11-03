import pandas as pd

# List of email addresses
email_addresses = [
    "career@fundtech.co.in",
    "career@braintreasure.com",
    "jobs@nanostuffs.com",
    "shalini.kanojia@vyomlabs.com",
    "recruitment_india@thedigitalgroup.net",
    "admin@sankalptech.com",
    "hr@sankalptech.com",
    "helpdesk@viraat.info",
    "admin@kalptech.in",
    "info@cliquemedia.com",
    "careers@highmark.in",
    "info@hexagonsearch.com",
    "resume@sysconnect.co.in",
    "careers@datamatics.com",
    "info@techizen.com",
    "PuneJobs@yardi.com",
    "mrinalini@edss.co.in",
    "vinita@handigital.com",
    "ruhee@handigital.com",
    "praveen.p@handigital.com",
    "hrd-india@magicsoftware.com",
    "careers@iwarelogic.com",
    "pavan.rathore@ascentt.com",
    "career@waiin.com",
    "cv@ashish.kumar@mayotech.in",
    "career@enzigma.com",
    "career@aditech.net",
    "jobs@airtightnetworks.com",
    "info@acceltree.com",
    "barada.kanta@accelfrontline.in",
    "hrd@accelfrontline.in",
    "career@accenture.com",
    "himani.chandra@randstad.in",
    "krutika.mehta@primefocusworld.com",
    "careers@xpointers.com",
    "hr@vilsoft.co.in",
    "hr@tejasit.com",
    "info@pelfinfotech.com",
    "hr@biyanitechnologies.com",
    "hrd@BenchmarkITsolutions.com",
    "chicho.varghese@capgemini.com",
    "getresponse09@gmail.com",
    "zycusindia@zycus.com",
    "jobs@designtechsys.com",
    "info@mtdhr.com",
    "jobs@jomaxservices.com",
    "pankit.lodaya@accenture.com",
    "email@abeltec.com",
    "fastrack@eq-technologic.com",
    "job@greytrix.com"
]

# Create a DataFrame
df = pd.DataFrame({'Email': email_addresses})

# Save the DataFrame to a CSV file with a .csv extension
df.to_csv('email_addresses.csv', index=False)
