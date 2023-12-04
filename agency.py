class AgencyClass:
    def __init__(self, code, name):
        self.name = name
        self.code = code

def get_agency(code):
    agency = AgencyClass(-99, "name")
    agency.code = code

    if code == 36001:
        agencyName = "Australia, Bureau of Meteorology (BoM)"
    if code == 36002:
        agencyName = "Australia, Joint Australian Facility for Ocean Observing Systems (JAFOOS)"
    if code == 36003:
        agencyName = "Australia, the Commonwealth Scientific and Industrial Research Organisation (CSIRO)"
    if code == 124001:
        agencyName = "Canada, Marine Environmental Data Service (MEDS)"
    if code == 124002:
        agencyName = "Canada, Institute of Ocean Sciences (IOS)"
    if code == 156001:
        agencyName = "China, The State Oceanic Administration"
    if code == 156002:
        agencyName = "China, Second Institute of Oceanography, State Oceanic Administration"
    if code == 156003:
        agencyName = "China, Institute of Ocean Technology"
    if code == 250001:
        agencyName = "France, Institut de Recherche pour le Developpement (IRD)"
    if code == 250002:
        agencyName = "France, Institut Francais de Recherche pour l'Exploitation de la mer (IFREMER)"
    if code == 276001:
        agencyName = "Germany, Bundesamt fuer Seeschiffahrt und Hydrographie (BSH)"
    if code == 276002:
        agencyName = "Germany, Institut fuer Meereskunde, Kiel"
    if code == 356001:
        agencyName = "India, National Institute of Oceanography (NIO)"
    if code == 356002:
        agencyName = "India, National Institute for Ocean Technology (NIOT)"
    if code == 356003:
        agencyName = "India, National Centre for Ocean Information Service"
    if code == 392001:
        agencyName = "Japan, Japan Meteorological Agency (JMA)"
    if code == 392002:
        agencyName = "Japan, Frontier Observational Research System for Global Change"
    if code == 392003:
        agencyName = "Japan, Japan Marine Science and Technology Centre (JAMSTEC)"
    if code == 410001:
        agencyName = "Republic of Korea, Seoul National University"
    if code == 410002:
        agencyName = "Republic of Korea, Korea Ocean Research and Development Institute  (KORDI)"
    if code == 410003:
        agencyName = "Republic of Korea, Meteorological Research Institute"
    if code == 540001:
        agencyName = "New Caledonia, Institut de Recherche pour le Developpement (IRD)"
    if code == 554001:
        agencyName = "New Zealand, National Institute of Water and Atmospheric Research (NIWA)"
    if code == 643001:
        agencyName = "Russian Federation, State Oceanographic Institute of Roshydromet"
    if code == 643002:
        agencyName = "Russian Federation, Federal Service for Hydrometeorology and Environmental Monitoring"
    if code == 724001:
        agencyName = "Spain, Instituto Espanol de Oceanografia"
    if code == 826001:
        agencyName = "United Kingdom, Hydrographic Office"
    if code == 826002:
        agencyName = "United Kingdom, Southampton Oceanography Centre (SOC)"
    if code == 840001:
        agencyName = "USA, NOAA Atlantic Oceanographic and Meteorological Laboratories (AOML)"
    if code == 840002:
        agencyName = "USA, NOAA Pacific Marine Environmental Laboratories (PMEL)"
    if code == 840003:
        agencyName = "USA, Scripps Institution of Oceanography (SIO)"
    if code == 840004:
        agencyName = "USA, Woods Hole Oceanographic Institution (WHOI)"
    if code == 840005:
        agencyName = "USA, University of Washington"
    if code == 840006:
        agencyName = "USA, Naval Oceanographic Office"
    if code == 1048575:
        agencyName = "Missing value"
    else:
        agencyName = "unknown"
        
    agency.name = agencyName

    return agency
