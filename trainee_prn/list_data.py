from edc_list_data import PreloadData

list_data = {
    'trainee_prn.deathcauseinfo': [
        ('No information will ever be available',
         'No information will ever be available'),
        ('Other, specify', 'Other, specify'),
        ('Autopsy', 'Autopsy'),
        ('Clinical record', 'Clinical record'),
        ('Information from physician/nurse/other health care provider',
         'Information from physician/nurse/other health care provider'),
        ('Information from participant\u2019s relatives or friends',
         'Information from participant\u2019s relatives or friends'),
        ('Information requested, still pending',
         'Information requested, still pending')
    ],
    'trainee_prn.causecategory': [
        ('No information will ever be available',
         'No information will ever be available'),
        ('Other, specify', 'Other, specify'),
        ('Cancer', 'Cancer'),
        ('HIV infection or HIV/AIDS-related diagnosis',
         'HIV infection or HIV/AIDS-related diagnosis'),
        ('Disease/injury unrelated to cancer or HIV',
         'Disease/injury unrelated to cancer or HIV'),
        ('Toxicity from cancer treatment (complications of chemotherapy, radiation, or surgery)',
         'Toxicity from cancer treatment (complications of chemotherapy, radiation, or surgery)'),
        ('Toxicity from HIV/AIDS treatment (HAART or treatment of HIV/AIDS-related diagnosis)',
         'Toxicity from HIV/AIDS treatment (HAART or treatment of HIV/AIDS-related diagnosis)')
    ]
}

preload_data = PreloadData(list_data=list_data)
