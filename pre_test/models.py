from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from django.forms import widgets as django_widgets
from Global_Constants import GlobalConstants

author = 'Kyubum Moon <mailto:moonx190@umn.edu>'

doc = """
행동실험 사전조사
"""


class Constants(BaseConstants):
    name_in_url = 'pre_test'
    players_per_group = None
    num_rounds = 1

    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES

    CRISIS_HIT_ADOLESCENCE, FEMALE, COLLEGE_STUDENTS, DISABLED, SMALL_SIZED_ENTERPRISE, OTHERS = 1,2,3,4,5,6

    REGISTRATION_TYPE = [
        [CRISIS_HIT_ADOLESCENCE,"위기청소년"],
        [FEMALE,"여성"],
        [COLLEGE_STUDENTS,"대학생"],
        [DISABLED,"장애인"],
        [SMALL_SIZED_ENTERPRISE,"소규모사업장"],
        [OTHERS,"기타"],
    ]

    PARENTS_OR_GRANDPARENTS, SIBLINGS, SPOUSE_OR_LOVER, CHILDREN, FRIEND_OR_UPPER_OR_LOWER_CLASSMEN, COLLEAUGES, TEACHER, MEDICAL_STAFF, OTHERS, NONE = 1,2,3,4,5,6,7,8,9,10

    SMOKING_CESSATION_HELPER = [
        [PARENTS_OR_GRANDPARENTS,"부모/조부모"],
        [SIBLINGS,"형제자매"],
        [SPOUSE_OR_LOVER,"배우자/애인"],
        [CHILDREN,"자녀"],
        [FRIEND_OR_UPPER_OR_LOWER_CLASSMEN,"친구/선후배"],
        [COLLEAUGES,"직장동료"],
        [TEACHER,"교사"],
        [MEDICAL_STAFF,"의료인"],
        [OTHERS,"기타"],
        [NONE,"없음"],
    ]

    TV_OR_RADIO_ADS, PLANCARD_POSTER_CATALOGUE, INTERNET, CLINIC_HANDOUT, ADVICE_FROM_THE_SURROUNDING, SMOKING_CESSATION_COUNSELING_CALL, EVENT, ADVICE_FROM_MEDICAL_STAFF, OTHERS = 1,2,3,4,5,6,7,8,9

    SMOKING_CESSATION_SUPPORT_SERVICE_REGISTRATION_PATH = [
        [TV_OR_RADIO_ADS,"TV 및 라디오 광고를 통해"],
        [PLANCARD_POSTER_CATALOGUE,"플랜카드, 포스터, 홍보책자 등을 통해"],
        [INTERNET,"인터넷을 통해"],
        [CLINIC_HANDOUT,"보건소 안내문을 통해"],
        [ADVICE_FROM_THE_SURROUNDING,"주변의 권유"],
        [SMOKING_CESSATION_COUNSELING_CALL,"금연상담전화를 통해"],
        [EVENT,"행사/이벤트를 통해"],
        [ADVICE_FROM_MEDICAL_STAFF,"의료진의 권고"],
        [기타,"OTHERS"],
    ]

    OROPHARYNGEAL_CANCER, LARYNX_CANCER, ESOPHAGEAL_CANCER, TRACHEAL_BRONCHIAL_AND_LUNG_CANCER, ACUTE_MYELOID_LEUKEMIA, STOMACH_CANCER, LIVER_CANCER, PANCREATIC_CANCER, KIDNEY_CANCER, URETER_CANCER, CERVICAL_CANCER, BLADDER_CANCER, COLORECTAL_CANCER, STROKE, BLINDNESS_CATARACT_SENILE_MACULAR_DEGENARTION, CONGENITAL_DEFECTS_DUE_TO_MATERNAL_SMOKING_ORAL_FACIAL_RUPTURE, PERIODONTITIS, JUVENILE_AORTIC_ANEURYSM_EARLY_ABDOMINAL_AORTIC_ATHEROSCLEROSIS, CORONARY_ARTERY_DISEASE, PNEUMONIA, ATHEROSCLEROTIC_LUNG_DISEASE_PERIPHERAL_VASCULAR_DISEASE, CHRONIC_OBSTRUCTIVE_PULMONARY_DISEASE_TUBERCULOSIS_ASTHMA_RESPIRATORY_EFFECTS_RHINTIS, DIABETES, EFFECTS_ON_FEMALE_REPRODUCTIVE_SYSTEM_AND_FETAL_GROWTH_FAILURE, HIP_FRACTURE, ECTOPIC_PREGNANCY, MALE_SEXUAL_FUNCTION_DEFECTION_ERECTILE_DYSFUNCTION, HYPERTENSION, RHEUMATOID_ARTHRITIS, HYPERLIPIDEMIA, OTHERS = range(1,32)

    DISEASE_HISTORY =[
        [OROPHARYNGEAL_CANCER,"구강인두암"],
        [LARYNX_CANCER,"후두암"],
        [ESOPHAGEAL_CANCER,"식도암"],
        [TRACHEAL_BRONCHIAL_AND_LUNG_CANCER,"기관, 기관지 및 폐암"],
        [ACUTE_MYELOID_LEUKEMIA,"급성 골수성 백혈병"],
        [STOMACH_CANCER,"위암"],
    ]

    NONE,WITHIN_TWO_WEEKS_UNSTABLE_ANGINA_OR_MYOCARDIAL_INFRACTION, SEVERE_ARRHYTHMIA, STROKE, LONG_TERM_DERMATITIS, SKIN_ALLERGY, PREGNANT_OR_BREAST_FEEDING, OTHERS = 1,2,3,4,5,6,7,8

    PRESENCE_OF_ADVERSE_EFFECT_OF_NICOTINE_PATCH = [
        [NONE,"없음"],
        [WITHIN_TWO_WEEKS_UNSTABLE_ANGINA_OR_MYOCARDIAL_INFRACTION,"최근 2주내 불안정 협심증 혹은 심근경색"],
        [SEVERE_ARRHYTHMIA,"중증 부정맥"],
        [STROKE,"뇌졸증"],
        [LONG_TERM_DERMATITIS,"장기적인 피부염(건선 등)"],
        [SKIN_ALLERGY,"피부 알레르기"],
        [PREGNANT_OR_BREAST_FEEDING,"임신중 또는 수유중"],
        [OTHERS,"기타"],
    ]

    CIGARETTE, LIQUID_E_CIGARETTE_NICOTINE, LIQUID_E_CIGARETTE_NO_NICOTINE,HOT_AND_BURN_E_CIGARETTE,CSV_TYPE_E_CIGARETTE, SNUS_TOBACCO, PIPE_TOBACCO, CIGAR, ROLLING_TOBACCO, HOOKAH, CHEWING_TOBACCO, SNUFF, NO_RESPONSE = range(1,14)

    TOBACCO_PRODUCT_IN_USE = [
        [CIGARETTE,"궐련(일반담배)"],
        [LIQUID_E_CIGARETTE_NICOTINE,"액상형 전자담배(니코틴 함유)"],
        [LIQUID_E_CIGARETTE_NO_NICOTINE,"액상형 전자담배(니코틴 미함유)"],
        [HOT_AND_BURN_E_CIGARETTE,"궐련형 전자담배(아이코스,릴,글로 등)"],
        [CSV_TYPE_E_CIGARETTE,"CSV형 전자담배(쥴,릴,베이퍼 등)"],
        [SNUS_TOBACCO,"머금는 담배(스누스)"],
        [PIPE_TOBACCO,"파이프담배"],
        [CIGAR,"엽궐련(시가)"],
        [ROLLING_TOBACCO,"각련(말아피우는 담배)"],
        [HOOKAH,"물담배"],
        [CHEWING_TOBACCO,"씹는담배"],
        [SNUFF,"냄새맡는 담배"],
        [NO_RESPONSE, "무응답"],
    ]

    NATIONAL_HEALTH_INSURANCE, MEDICAL_ALLOWANCE_FOR_RECIPIENTS_OF_ALLOWANCE_FOR_SURVIVAL, NO_IDEA, NOT_ENROLLED, NO_RESPONSE_OR_REFUSAL_TO_ANSWER = 1,2,3,4,5

    MEDICAL_GUARANTEE = [
        [NATIONAL_HEALTH_INSURANCE,"국민건강보험"],
        [MEDICAL_ALLOWANCE_FOR_RECIPIENTS_OF_ALLOWANCE_FOR_SURVIVAL,"의료급여(기초수급자 및 차상위)"],
        [NO_IDEA,"모름"],
        [NOT_ENROLLED,"미가입"],
        [NO_RESPONSE_OR_REFUSAL_TO_ANSWER,"무응답/응답거부"],
    ]

    NO_SCHOOLING, ELEMENTARY_SCHOOL_GRADUATION_OR_LOWER, MIDDLE_SCHOOL_GRADUATION_OR_LOWER, HIGH_SCHOOL_GRADUATION_OR_LOWER, COMMUNITY_COLLEGE_OR_UNIVERSITY_GRADUATION_OR_LOWER, COMPLETION_OF_GRADUATE_SCHOOL_EDUCATION_OR_HIGHER, NO_IDEA, NO_RESPONSE_OR_REFUSAL_TO_ANSWER = 1,2,3,4,5,6,7,8

    FINAL_SCHOOLING_LEVEL = [
        [NO_SCHOOLING,"무학"],
        [ELEMENTARY_SCHOOL_GRADUATION_OR_LOWER, "초등학교 졸업이하"],
        [MIDDLE_SCHOOL_GRADUATION_OR_LOWER, "중학교 졸업이하"],
        [HIGH_SCHOOL_GRADUATION_OR_LOWER, "고등학교 졸업이하"],
        [COMMUNITY_COLLEGE_OR_UNIVERSITY_GRADUATION_OR_LOWER, "전문대/대학교 졸업이하"],
        [COMPLETION_OF_GRADUATE_SCHOOL_EDUCATION_OR_HIGHER, "대학원 수료이상"],
        [NO_IDEA,"모름"],
        [NO_RESPONSE_OR_REFUSAL_TO_ANSWER,"무응답/응답거부"],
    ]

    MANAGER, PROFESSIONAL_AND_RELATED_WORKERS, OFFICE_WORKERS, SERVICE_WORKERS, SALES_WORKERS, AGICULURE_FISHERY_TRAINED_WORKERS, SKILL_AND_RELATED_SKILL_WORKERS, DEVICE_MACHINE_OPERATORS_AND_ASSEMBLING_WORKERS, SIMPLE_LABOR_WORKERS, SOLDIERS, ADOLESCENCE_AGE_TWENTYFOUR_OR_YOUNGER, COLLEGE_STUDENTS, NO_JOB, OTHERS, NO_IDEA, NO_RESPONSE_OR_REFUSAL_TO_ANSWER = range(1,17)

    OCCUPATION = [
        [MANAGER,"관리자"],
        [PROFESSIONAL_AND_RELATED_WORKERS,"전문가 및 관련종사자"],
        [OFFICE_WORKERS,"사무 종사자"],
        [SERVICE_WORKERS,"서비스 종사자"],
        [SALES_WORKERS,"판매 종사자"],
        [AGICULURE_FISHERY_TRAINED_WORKERS,"농림어업 숙련 종사자"],
        [SKILL_AND_RELATED_SKILL_WORKERS,"기능 및 관련기능 종사자"],
        [DEVICE_MACHINE_OPERATORS_AND_ASSEMBLING_WORKERS,"장치,기계조작 및 조립 종사자"],
        [SIMPLE_LABOR_WORKERS,"단순 노무 종사자"],
        [SOLDIERS,"군인"],
        [ADOLESCENCE_AGE_TWENTYFOUR_OR_YOUNGER,"청소년(만 24세 이하)"],
        [COLLEGE_STUDENTS,"대학생"],
        [NO_JOB,"무직"],
        [OTHERS,"기타"],
        [NO_IDEA,"모름"],
        [NO_RESPONSE_OR_REFUSAL_TO_ANSWER,"무응답/응답거부"],
    ]

    SELF_WILL_POWER, PUBLIC_CLINIC_SMOKING_CESSATION, REGIONAL_SMOKING_CESSSATION_SUPPORT_CENTER, SMOKING_CESSATION_HOT_LINE, SMOKING_CESSATION_TREATMENT_AT_HOSPITALS_OR_CLINICS, OTHER_SERVICES_OR_ALTERNATIVE_ITEMS_USAGE = 1,2,3,4,5,6

    SMOKING_CESSATION_METHOD = [
        [SELF_WILL_POWER,"자기 의지"],
        [PUBLIC_CLINIC_SMOKING_CESSATION, "보건소 금연클리닉"],
        [REGIONAL_SMOKING_CESSSATION_SUPPORT_CENTER, "지역금연지원센터"],
        [SMOKING_CESSATION_HOT_LINE, "금연상담전화"],
        [SMOKING_CESSATION_TREATMENT_AT_HOSPITALS_OR_CLINICS,"병의원 금연치료"],
        [OTHER_SERVICES_OR_ALTERNATIVE_ITEMS_USAGE,"기타서비스 또는 대체용품 사용"],
    ]

    LACK_OF_WILL_POWER, SYMPTOMS_OF_TOBACCO_WITHDRAWAL, STRESS, TEMPTATION_FROM_SURROUNDING, WEIGHT_GAIN_AFTER_SMOKING_CESSATION, OTHERS = 1,2,3,4,5,6

    REASON_FOR_FAILURE_OF_SMOKING_CESSATION = [
        [LACK_OF_WILL_POWER,"본인의 의지가 약해서"],
        [SYMPTOMS_OF_TOBACCO_WITHDRAWAL,"금단증상 때문에"],
        [STRESS,"스트레스가 쌓여서"],
        [TEMPTATION_FROM_SURROUNDING,"주위의 유혹에 의해서"],
        [WEIGHT_GAIN_AFTER_SMOKING_CESSATION,"금연 후 체중이 늘어서"],
        [OTHERS,"기타"]
    ]

    SUGGESTION_FROM_FAMILY_OR_SURROUNDING, FOR_PERSONAL_HEALTH_WORSENING_OF_CURRENT_DISEASE_AND_PREVENTION_OF_FUTURE_ILLNESSES, ECONOMIC_REASON, ENVIRONMENTAL_REASON, TO_KEEP_A_CLEAN_IMAGE, TO_PREVENT_ADVERSE_EFFECT_ON_PEERS_HEALTH, TO_SHOW_MY_SMOKING_CESSATION_RESOLUTION, SOCIAL_NORMS_AGAINST_SMOKERS,OTHERS = 1,2,3,4,5,6,7,8,9

    REASON_TO_QUIT_SMOKING_THIS_TIME = [
        [SUGGESTION_FROM_FAMILY_OR_SURROUNDING,"가족 혹은 주변사람들의 권유"],
        [FOR_PERSONAL_HEALTH_WORSENING_OF_CURRENT_DISEASE_AND_PREVENTION_OF_FUTURE_ILLNESSES,"현재 질병악화 및 장래 질병발생예방"],
        [ECONOMIC_REASON,"담뱃값 인상 등 경제적 이유"],
        [ENVIRONMENTAL_REASON,"금연구역 확대 등 환경적 이유"],
        [TO_KEEP_A_CLEAN_IMAGE,"꺠끗한 이미지 관리를 위해서(예:입 냄새가 고약, 옷에 담배 냄새가 뱀"],
        [TO_PREVENT_ADVERSE_EFFECT_ON_PEERS_HEALTH,"꺠끗한 이미지 관리를 위해서(예:입 냄새가 고약, 옷에 담배 냄새가 뱀"],
        [TO_SHOW_MY_SMOKING_CESSATION_RESOLUTION,"금연의지를 보여주기 위해"],
        [SOCIAL_NORMS_AGAINST_SMOKERS,"흡연자에 대한 사회적 시선 때문"],
        [OTHERS,"기타"],
    ]

    WHEN_ONE_WAKES_UP_IN_THE_MORNING, BEFORE_GOING_TO_BED, AFTER_MEAL, AT_A_RESTROOM_OR_AFTER_TAKING_A_SHOWER, RESTING_TIME, BEHAVIORAL_CIRCUMSTNACES, POSITIVE_CIRCUMSTNACES, NEGATIVE_CIRCUMSTANCES, WHEN_BEING_WITH_A_SMOKER_OR_WITNESSING_A_SMOKER, OTHERS = 1,2,3,4,5,6,7,8,9,10

    THE_HARDEST_TIME_TO_STAND_AGAINST_DESIRE_TO_SMOKE = [
            [WHEN_ONE_WAKES_UP_IN_THE_MORNING,"아침에 일어나자마자"],
            [BEFORE_GOING_TO_BED,"잠들기 전"],
            [AFTER_MEAL,"식사 후"],
            [AT_A_RESTROOM_OR_AFTER_TAKING_A_SHOWER,"화장실에서/샤워 후"],
            [RESTING_TIME,"휴식시간"],
            [BEHAVIORAL_CIRCUMSTNACES,"습관적 상황에서(활력이 필요할 때/담배를 피우지 않음을 깨달을 때, 술/커피 마실 때, 혼자 있거나 무언가 기다릴 때 등"],
            [POSITIVE_CIRCUMSTNACES,"긍정적 상황(친구나 가족과 함께 있을 때, 대화나 피로를 풀 때"],
            [NEGATIVE_CIRCUMSTANCES,"부정적 상황(스트레스 받을 때, 일이 뜻대로 안될 때, 화날 때 등"],
            [WHEN_BEING_WITH_A_SMOKER_OR_WITNESSING_A_SMOKER,"흡연자와 같이 있거나, TV의 배우 또는 주위 흡연자의 모습을 보았을 때"],
            [OTHERS,"기타"],
    ]

    SMOKING_CESSATION_MOTIVATION = [
        [1, "(0)"],
        [2, "(1)"],
        [3, "(2)"],
        [4, "(3)"],
        [5, "(4)"],
        [6, "(5)"],
        [7, "(6)"],
        [8, "(7)"],
        [9, "(8)"],
        [10, "(9)"],
        [11, "(10)"],
    ]

    SMOKING_CESSATION_CONFIDENCE = [
        [1, "(0)"],
        [2, "(1)"],
        [3, "(2)"],
        [4, "(3)"],
        [5, "(4)"],
        [6, "(5)"],
        [7, "(6)"],
        [8, "(7)"],
        [9, "(8)"],
        [10, "(9)"],
        [11, "(10)"],
    ]
    SMOKING_CESSATION_READINESS = [
        [1, "(0)"],
        [2, "(1)"],
        [3, "(2)"],
        [4, "(3)"],
        [5, "(4)"],
        [6, "(5)"],
        [7, "(6)"],
        [8, "(7)"],
        [9, "(8)"],
        [10, "(9)"],
        [11, "(10)"],
    ]
    FIRST_TOBACCO_TIME = [
        [1, "(3) 5분 이내"],
        [2, "(2) 6~30분 사이"],
        [3, "(1) 31분~1시간 사이"],
        [4, "(0) 1시간 이후"],
    ]

    NICOTINE_DEPENDENCY_YESNO = [
        [1, "(1) 예"],
        [2, "(0) 아니오"],
    ]

    THE_BEST_TIME_FOR_SMOKING_IN_A_DAY = [
        [1, "(1) 아침 첫 담배"],
        [2, "(0) 그 외의 담배"],
    ]

    SMOKING_AMOUNT_COUNT_PER_DAY = [
        [1, "(0) 10개비 이하"],
        [2, "(1) 11~20개비"],
        [3, "(2) 21~30개비"],
        [4, "(3) 31개비 이상"],
    ]

    SMOKING_TYPE_LICKERT_SCALE = [
        [1, "전혀 그렇지 않다"],
        [2, "그렇지 않은 편이다"],
        [3, "간혹 그렇다"],
        [4, "자주 그렇다"],
        [5, "항상 그렇다"],
    ]

    SERVICE_SATISFACTION_LICKERT_SCALE = [
        [1, "매우 그렇다"],
        [2, "그렇다"],
        [3, "보통이다"],
        [4, "그렇지 않다"],
        [5, "전혀 그렇지 않다"],
    ]

    HEALTH_STATUS = [
        [1, "매우 건강함"],
        [2, "건강한 편"],
        [3, "보통"],
        [4, "허악한 편"],
        [5, "매우 허약함"],
    ]

    STRESS_MEASURE = [
        [1, "전혀 받지 않음"],
        [2, "별로 받지 않음"],
        [3, "그저 그런 편임"],
        [4, "약간 받는 편"],
        [5, "매우 많이 받음"],
    ]

    FUTURE_SMOKING_CESSATION_PLAN = [
        [1, "금연에 대해 생각해 본 적 없음"],
        [2, "향후 6개월 이내에 금연할 계획이 있음"],
        [3, "1개월 이내에 금연할 계획이 있음"],
        [4, "금연을 실천한 지 1일 이상이 지났음"],
        [5, "금연을 실천한 지 6개월 이상 되었음"],
    ]

    SMOKING_CESSATION_PRE_SURVEY_LICKERT_SCALE = [
        [1, "전혀 그렇지 않다"],
        [2, "그렇지 않다"],
        [3, "보통"],
        [4, "그렇다"],
        [5, "매우 그렇다"],
    ]

    EXPERIENCE_SCALE = [
        [1, "전혀 욕구가 없다"],
        [2, "아무욕구도 없다"],
        [3, "보통"],
        [4, "항상"],
        [5, "매우 강하다"],
    ]
    SMOKING_CESSATION_PRE_SURVEY_CONFIDENCE = [
        [1, "전혀 자신없다"],
        [2, "자신없다"],
        [3, "보통"],
        [4, "자신있다"],
        [5, "매우 자신있다"],
    ]

    MALE, FEMALE = 1,2

    GENDER = [
        [MALE, "남성"],
        [FEMALE,"여성"],
    ]

    SEOUL, INCHEON, GYEONGGI, GANGWON, SEJONG, CHUNGNAM, CHUNGBUK, DAEJEON, DAEGU, KYUNGBUK, KYUNGNAM, ULSAN, BUSAN, CHEONBUK, CHEONNAM, GWANGJU, JEJU=range(1,18)
    REGION_CHOICE = [
        [SEOUL, "서울"],
        [INCHEON, "인천"],
        [GYEONGGI, "경기도"],
        [GANGWON, "강원도"],
        [SEJONG, "세종"],
        [CHUNGNAM, "충청남도"],
        [CHUNGBUK, "충청북도"],
        [DAEJEON, "대전"],
        [DAEGU, "대구"],
        [KYUNGBUK, "경상북도"],
        [KYUNGNAM, "경상남도"],
        [ULSAN, "울산"],
        [BUSAN, "부산"],
        [CHEONBUK, "전라북도"],
        [CHEONNAM, "전라남도"],
        [GWANGJU, "광주"],
        [JEJU,"제주도"],
    ]

    BIGCITY, SMALLCITY, EUPMYUN, SPECIAL=range(1,5)

    REGION_SIZE_CHOICE = [
        [BIGCITY, "대도시 (특별/광역시 - 서울, 부산, 대구, 인천, 광주, 대전, 울산)"],
        [SMALLCITY, "특별/광역시가 아닌 그 외 지역"],
        [EUPMYUN, "읍면 지역(ex. ○○시 ○○읍/면)"],
        [SPECIAL, "특수 지역(도서·벽지 지역)"],
    ]

    NOT_MARRIED, MARRIED, DIVORCED_BEREAVEMENT, MARRIAGE_OTHER = 1, 2, 3, 4

    MARRIAGE_CHOICE = [
        [NOT_MARRIED, "결혼안함"],
        [MARRIED, "결혼함"],
        [DIVORCED_BEREAVEMENT, "이혼/사별함"],
        [MARRIAGE_OTHER, "기타"],
    ]

    FULLTIME, PARTTIME, FREELANCER, NO_JOB_WITHIN_PAST_SIX_MONTHS = 1,2,3,4

    JOB_POSITION = [
        [FULLTIME,"전일제 근무자"],
        [PARTTIME, "파트타임 근무자"],
        [FREELANCER,"프리랜서"],
        [NO_JOB_WITHIN_PAST_SIX_MONTHS, "최근 6개월 이내 근무경력 없음"],
    ]

    PUBLIC, GOV, BIGFIRM, MID_SIZED_FIRM, SMALLFIRM, ETC, NOT_WORKING = 1,2,3,4,5,6,7,9

    FIRM_TYPE = [
        [PUBLIC, "공기업·준정부기관·기타 공공기관"],
        [GOV, "공무원"],
        [BIGFIRM, "사기업-대기업"],
        [MID_SIZED_FIRM,"사기업-중견기업"],
        [SMAllFIRM,"사기업-중소·벤처기업"],
        [ETC,"기타(직접입력)"],
        [NOT_WORKING,"현재 근무중이 아님"],
    ]

    UNDER5, OVER5UNDER50, OVER50UNDER100, OVER100UNDER200,OVER200UNDER300,OVER300, NOT_WORKING = 1,2,3,4,5,6,9

    FIRM_SIZE = [
        [UNDER5, "5인 미만"],
        [OVER5UNDER50, "5인 이상~50인 미만"],
        [OVER50UNDER100, "50인 이상~100인 미만"],
        [OVER100UNDER200, "100인 이상~200인 미만"],
        [OVER200UNDER300, "200인 이상~300인 미만"],
        [OVER300, "300인 이상"],
        [NOT_WORKING, "현재 근무중이 아님"],
    ]

    INCOME_LEVEL_CHOICE = [
        [1, "없음"],
        [2, "150만원 미만"],
        [3, "150만원 이상 300만원 미만"],
        [4, "300만원 이상 450만원 미만"],
        [5, "450만원 이상 600만원 미만"],
        [6, "600만원 이상 750만원 미만"],
        [7, "750만원 이상"],

    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    registration_category = models.IntegerField(
        label = "귀하의 등록유형은 어떻게 되십니까?",
        choices=Constants.REGISTRATION_TYPE,
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_cessation_start_date = models.IntegerField(
        label="귀하의 금연시작일을 20200120 (년월일 : 한 자릿수 월이나 일일 경우 07등으로 입력) 형식으로 입력해주시기 바랍니다.",
    )

    registration_date = models.IntegerField(
        label = "금연프로그램 등록일을 20200120 (년월일 : 한 자릿수 월이나 일일 경우 07등으로 입력) 형식으로 입력해주시기 바랍니다."
    )

    smoking_cessation_resolution_date = models.IntegerField(
        label="귀하의 금연결심일을 20200120 (년월일 : 한 자릿수 월이나 일일 경우 07등으로 입력) 형식으로 입력해주시기 바랍니다."
    )
    
