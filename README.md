Care is a prototype Health Care protocol language.

To run CARE, you just need version of Python 3. Download the zipfile, extract it to your directory of choice.
After extracting, navigate to the main CARE_PL with your CMD or Terminal of choice, and execute:
                
                                        python -m CARE.care

 Here is a quick run-down:

    To create a patient simply write the patient's name followed by .create()
    ex Angel.create()

    To remove a patient simply write the patient's name followed by .remove
    ex Angel.remove()
    
    To add a symptom: use the patient's name then use .has() with symptom
    ex: Angel.has(fever)
    
    To view list of symptoms: use the keyword "Symptom"
    ex: CARE >> symptom
    
    To list a patient's symptom's use .list() 
    ex: Angel.list()

    To auto diagnose patient simply write the patient's name followed by .diagnose()
    ex: Angel.diagnose()
    
    To define your own illnesses simply write ailment(ILLNESS).create() 
    ex: ailment(flu).create() 
    
    To add symtpoms to your defined illness write ailment(ILLNESS).add(SYMPTOM) 
    ex: ailment(flu).add(fever) 
    
    To add patient to queue write the keyword QUEUE followed by the patient's name
    ex: queue(Angel)
    
    To review a patient and remove from queue use the attend keyword
    ex: attend()
    
With these basic functions, it will be easier to manage your patients and their symptoms  
