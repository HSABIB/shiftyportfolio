from projects.models import *


list_categories = [
    'Artificial intelligence (AI)',
    'Internet of things (IOT)',
    'Web developement',
    'Mobile developement',
    'Third party integration',
    'Data analysis',
    'Cloud',
    'Business intelligence',
    'Consultancy',
]

list_projects = [
    {
        'slogan'    :      "Ecommerce Solution",
        'flabel'    :      "Ecommerce",
        'llabel'    :      "Solution",
        'miniature' :      "https://res.cloudinary.com/dbarj1xvr/image/upload/v1613458941/001_swvfex.jpg",
        'categories':       [2, 3, 4, 6]
    },{
        'slogan'    :      "Custom shopify application",
        'flabel'    :      "Shopify",
        'llabel'    :      "App",
        'miniature' :      "https://res.cloudinary.com/dbarj1xvr/image/upload/v1613458590/002_kzsjbl.jpg",
        'categories':       [2, 3, 4, 5, 6]
    },{
        'slogan'    :      "Web application",
        'flabel'    :      "Web",
        'llabel'    :      "Application",
        'miniature' :      "https://res.cloudinary.com/dbarj1xvr/image/upload/v1613458705/muhannad-ajjan-sL2BRR1cuvM-unsplash_vslbes.jpg",
        'categories':       [2, 3, 4, 6, 8]
    },{
        'slogan'    :      "Mobile application",
        'flabel'    :      "Mobile",
        'llabel'    :      "Application",
        'miniature' :      "https://res.cloudinary.com/dbarj1xvr/image/upload/v1613458753/markus-winkler-4TBdESUNuFg-unsplash_fm7pnl.jpg",
        'categories':       [3, 4, 6, 8]
    },{
        'slogan'    :      "Data analysis",
        'flabel'    :      "Data",
        'llabel'    :      "Analysis",
        'miniature' :      "https://res.cloudinary.com/dbarj1xvr/image/upload/v1613458274/003_cc5vp7.jpg",
        'categories':       [0, 2, 8, 5]
    },{
        'slogan'    :      "Cloud Migration & Admin Services",
        'flabel'    :      "Cloud",
        'llabel'    :      "Services",
        'miniature' :      "https://res.cloudinary.com/dbarj1xvr/image/upload/v1613459799/c-dustin-K-Iog-Bqf8E-unsplash_pqzpsd.jpg  ",
        'categories':       [4, 6, 8]
    },{
        'slogan'    :      "Architecture, Data & Platform Design",
        'flabel'    :      "Architecture",
        'llabel'    :      "Platform",
        'miniature' :      "https://res.cloudinary.com/dbarj1xvr/image/upload/v1613460027/luke-chesser-JKUTrJ4vK00-unsplash_e7rfjp.jpg",
        'categories':       [8, 6, 4, 2, 3]
    },{
        'slogan'    :      "Third-Party Software Integration",
        'flabel'    :      "Software",
        'llabel'    :      "Integration",
        'miniature' :      "https://res.cloudinary.com/dbarj1xvr/image/upload/v1613459814/jj-ying-7JX0-bfiuxQ-unsplash_mvbcyd.jpg",
        'categories':       [4, 2]
    },{
        'slogan'    :      "Business Intelligence and Optimization",
        'flabel'    :      "Business",
        'llabel'    :      "Intelligence",
        'miniature' :      "https://res.cloudinary.com/dbarj1xvr/image/upload/v1613459863/floriane-vita-FyD3OWBuXnY-unsplash_zccfpx.jpg",
        'categories':       [7, 8, 5]
    },{
        'slogan'    :      "Artificial Intelligence and Machine learning",
        'flabel'    :      "Artificial",
        'llabel'    :      "Intelligence",
        'miniature' :      "https://res.cloudinary.com/dbarj1xvr/image/upload/v1613459931/joel-filipe-VuwAfoHpxgs-unsplash_xhninp.jpg",
        'categories':       [0, 7, 6, 5]
    },{
        'slogan'    :      "Internet of things",
        'flabel'    :      "Internet",
        'llabel'    :      "Of Things",
        'miniature' :      "https://res.cloudinary.com/dbarj1xvr/image/upload/v1613458880/thisisengineering-raeng-32PpagSzeGs-unsplash_bj2b78.jpg",
        'categories':       [1, 7, 6]
    }
]

forloop_counter = 0
for category_label in list_categories :
    number = 100 + forloop_counter
    Category.objects.create(number=number, label=category_label)
    forloop_counter += 1

forloop_counter = 0
for project_json in list_projects :
    project_db = Project.objects.create(
        flabel=project_json.get('flabel'),
        llabel=project_json.get('llabel'),
        slogan=project_json.get('slogan'),
        miniature=project_json.get('miniature'),
        deleted=True if forloop_counter > 0 else False
    )
    for project_category in project_json.get('categories') :
        number = 100 + project_category
        category_db = Category.objects.get(number=number)
        ProjectCategory.objects.create( project=project_db, category=category_db )
    forloop_counter += 1
