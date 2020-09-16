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
from Global_Constants import GlobalConstants

author = 'Kyubum Moon<mailto:moonx190@umn.edu>'

doc = """
행동강화 물품이 금연동기강화 및 금연유지에 미치는 효과분석 온라인설문
"""


class Constants(BaseConstants):
    name_in_url = 'online_survey'
    players_per_group = None
    num_rounds = 1
    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES
    BINARY_POSSESSION = GlobalConstants.BINARY_POSSESSION
    BORN_YEAR_MIN = 1959
    BORN_YEAR_MAX = 2000

    FULLTIME, PARTTIME, FREELANCER, UNPAID = 1, 2, 3, 99
    JOB_POSITION = [
        [FULLTIME, "전일제 근무자"],
        [PARTTIME, "파트타임 근무자"],
        [FREELANCER, "프리랜서"],
        [UNPAID, "최근 6개월 이내 근무경력 없음"]
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(
        label="귀하의 성별은 어떻게 되십니까?",
        choices=[
            [1, "남성"],
            [2, "여성"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    born_year = models.IntegerField(
        label="귀하의 출생년도를 기입해주세요. (대상자: 만20세~59세:2000년생부터 1960년생까지)",
        choices=range(Constants.BORN_YEAR_MAX, Constants.BORN_YEAR_MIN, -1),
    )

    job_position = models.IntegerField(
        label="직장(일)에서 귀하의 지위는 무엇입니까?",
        choices=Constants.JOB_POSITION,
        widget=widgets.RadioSelect,
    )

    smoking_in_lifetime_yesno = models.IntegerField(
        label="지금까지 살아오는 동안 담배를 피운 적 있습니까? (여기에서 담배는, 일반 담배(궐련)과 액상형/궐련형 전자담배 모두를 포괄합니다.)",
        choices=[
            [999, "예. 5갑(100개비) 미만"],
            [1, "예. 5갑(100개비) 이상"],
            [9999, "아니오. 피운 적 없음"],
        ],
        widget=widgets.RadioSelect,
    )
    within_past_one_year_smoking_cessation_attempted = models.IntegerField(
        label="최근 1년 동안 담배를 끊고자 하루(24시간) 이상 금연한 적이 있습니까?",
        choices=[
            [1, "예"],
            [99999, "아니오"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    region = models.IntegerField(
        label="귀하의 거주 지역을 선택해주세요.",
        choices=[
            [1, "서울"],
            [2, "인천"],
            [3, "경기도"],
            [4, "강원도"],
            [5, "세종"],
            [6, "충청남도"],
            [7, "충청북도"],
            [8, "대전"],
            [9, "대구"],
            [10, "경상북도"],
            [11, "경상남도"],
            [12, "울산"],
            [13, "부산"],
            [14, "전라북도"],
            [15, "전라남도"],
            [16, "광주"],
            [17, "제주도"],
        ],
        widget=widgets.RadioSelect,
    )

    region_size = models.IntegerField(
        label="귀하의 거주지의 지역규모를 선택해주세요.",
        choices=[
            [1, "대도시(특별/광역시-서울, 부산, 대구, 인천, 광주, 대전, 울산)"],
            [2, "중소도시(특별/광역시가 아닌 그 외 지역)"],
            [3, "읍면지역(ex. ○○시 ○○읍/면)"],
            [4, "특수지역(도서·벽지 지역)"],
        ],
        widget=widgets.RadioSelect,
    )

    marriage = models.IntegerField(
        label="귀하의 혼인상태를 선택해주십시오",
        choices=[
            [1, "결혼안함"],
            [2, "결혼함"],
            [3, "이혼/사별함"],
            [4, "기타"],
        ],
        widget=widgets.RadioSelect,
    )

    final_schooling = models.IntegerField(
        label="귀하의 최종 학력을 선택해주세요",
        choices=[
            [1, "무학"],
            [2, "초등학교 졸업이하"],
            [3, "중학교 졸업이하"],
            [4, "고등학교 졸업이하"],
            [5, "전문대/대학교 졸업이하"],
            [6, "대학원 수료이상"],
        ],
        widget=widgets.RadioSelect,
    )

    occupation = models.IntegerField(
        label="귀하의 직업을 선택해주세요",
        choices=[
            [1, "관리자"],
            [2, "전문가 및 관련종사자"],
            [3, "사무 종사자"],
            [4, "서비스 종사자"],
            [5, "판매 종사자"],
            [6, "농림어업 숙련 종사자"],
            [7, "기능 및 관련기능 종사자"],
            [8, "장치, 기계조작 및 조립 종사자"],
            [9, "단순 노무 종사자"],
            [10, "군인"],
            [11, "기타(직접입력)"],
        ],
        widget=widgets.RadioSelect,
    )

    occupation_op = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    firm_type = models.IntegerField(
        label="귀하께서 현재 근무하시는 기업의 유형은 다음 중 무엇입니까?",
        choices=[
            [1, "공기업·준정부기관·기타 공공기관"],
            [2, "공무원"],
            [3, "사기업-규모별: 대기업"],
            [4, "사기업-규모별: 중견기업"],
            [5, "사기업-규모별: 중소·벤처기업"],
            [6, "사기업-규모별: 소기업 및 소상공인"],
            [7, "기타(위에 해당하지 않는 경우 자유 입력: )"],
        ],
        widget=widgets.RadioSelect,
    )

    firm_type_op = models.StringField(
        label="기타(위에 해당하지 않는 경우 자유 입력)",
        blank=True,
    )

    firm_size = models.IntegerField(
        label="현재 근무하시는 사업장 규모를 다음 중 선택해주십시오",
        choices=[
            [1, "5인 미만"],
            [2, "5인 이상~50인 미만"],
            [3, "50인 이상~100인 미만"],
            [4, "100인 이상~200인 미만"],
            [5, "200인 이상~300인 미만"],
            [6, "300인 이상"],
        ],
        widget=widgets.RadioSelect,
    )

    household_income = models.IntegerField(
        label="최근 6개월 평균 가구소득액(즉, 가족구성원 전체의 수입 합산액)은 어떻게 되십니까? 월별 세후 실질 수령액 기준으로 선택해 주십시오.",
        choices=[
            [1, "없음"],
            [2, "150만원 미만"],
            [3, "150만원 이상 300만원 미만"],
            [4, "300만원 이상 450만원 미만"],
            [5, "450만원 이상 600만원 미만"],
            [6, "600만원 이상 750만원 미만"],
            [7, "750만원 이상"],
        ],
        widget=widgets.RadioSelect,
    )

    num_drink_not = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    drink_freq_1 = models.IntegerField(
        label="일주일에 (__)번",
        choices=range(1, 8),
        blank=True,
    )

    drink_freq_2 = models.IntegerField(
        label="한 달에 (__)번",
        choices=range(1, 31),
        blank=True,
    )

    drink_freq_3 = models.IntegerField(
        label="1년에 (__)번",
        choices=range(1, 13),
        blank=True,
    )

    alc_avg_1_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_1_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_1_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_1_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_avg_2_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_2_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_2_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_2_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_avg_3_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_3_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_3_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_3_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_avg_4_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_4_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_4_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_4_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_avg_5_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_5_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_5_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_5_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    high_act_day = models.IntegerField(
        label="",
        choices=range(0, 8),
    )

    high_act_hour = models.IntegerField(
        label="",
        choices=range(0, 24),
    )

    high_act_min = models.IntegerField(
        label="",
        choices=range(0, 60),
    )

    mid_act_day = models.IntegerField(
        label="",
        choices=range(0, 8),
    )

    mid_act_hour = models.IntegerField(
        label="",
        choices=range(0, 24),
    )

    mid_act_min = models.IntegerField(
        label="",
        choices=range(0, 60),
    )

    muscle_act_days = models.IntegerField(
        label="",
        choices=range(0, 8),
    )

    overall_health_evaluation = models.IntegerField(
        label="귀하가 생각하는 본인의 현재 건강상태는 어떻습니까?",
        choices=range(0, 11),
        blank=True,
    )
    overall_stress_evaluation = models.IntegerField(
        label="평소 귀하의 스트레스 정도는 어떻습니까?",
        choices=range(0, 11),
        blank=True,
    )

    tobacco_product_in_use_1 = models.BooleanField(
        label="궐련(일반담배)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_2 = models.BooleanField(
        label="액상형 전자담배(니코틴 함유)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_3 = models.BooleanField(
        label="액상형 전자담배(니코틴 미함유)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_4 = models.BooleanField(
        label="궐련형 전자담배(아이코스,릴,글로 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_5 = models.BooleanField(
        label="CSV형 전자담배(쥴, 릴 베이퍼 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_6 = models.BooleanField(
        label="머금는 담배(스누스)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_7 = models.BooleanField(
        label="파이프담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_8 = models.BooleanField(
        label="엽권련(시가)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_9 = models.BooleanField(
        label="각련(말아피우는 담배)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_10 = models.BooleanField(
        label="물담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_11 = models.BooleanField(
        label="씹는담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_12 = models.BooleanField(
        label="냄새맡는 담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    do_you_smoke_tobacco = models.IntegerField(
        label="현재 일반담배(궐련)를 피우십니까?",
        choices=[
            [1, "매일피움"],
            [2, "가끔피움"],
            [3, "과거엔 피웠으나, 현재 피우지 않음"],
            [4, "과거에도, 현재에도 피운 적 없음"],
        ],
        widget=widgets.RadioSelect,
    )

    first_time_to_finish_one_stick_of_tobacco = models.IntegerField(
        label="처음으로 일반담배(궐련) 한 개비를 다 피운 시기는 언제입니까? (만나이로 대답해주시기 바랍니다.)",
        choices=range(100),
        blank=True,
    )

    first_time_to_finish_one_stick_or_more = models.IntegerField(
        label="매일 한 개비 이상의 일반담배(궐련)를 피운 시기는 언제입니까? (만나이로 대답해주시기 바랍니다.)",
        choices=range(100),
        blank=True,
    )

    avg_daily_tobacco_smoking_amount = models.IntegerField(
        label="하루 평균 일반담배(궐련) 흡연량",
        blank=True,
    )

    within_past_month_tobacco_smoking_days = models.IntegerField(
        label="최근 1달 간 일반담배(궐련) 흡연일수",
        choices=range(1, 31),
        blank=True,
    )

    tobacco_sticks_per_day = models.IntegerField(
        label="일반담배(궐련)를 흡연한 날 하루 평균 흡연량(기준: 개비)",
        choices=range(101),
        blank=True,
    )

    past_tobacco_smoking_years = models.IntegerField(
        label="과거 일반담배(궐련) 흡연기간(연수)",
        choices=range(101),
        blank=True,
    )
    past_tobacco_smoking_months = models.IntegerField(
        label="과거 일반담배(궐련) 흡연기간(개월수(0-11))",
        choices=range(12),
        blank=True,
    )
    past_tobacco_sticks_per_day = models.IntegerField(
        label="과거 일반담배(궐련)를 피울 때 하루 평균 흡연량(개비)",
        choices=range(101),
        blank=True,
    )

    hardest_time_to_resist_smoking_1 = models.BooleanField(
        label="아침에 일어나자마자",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_2 = models.BooleanField(
        label="잠들기 전",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_3 = models.BooleanField(
        label="식사",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_4 = models.BooleanField(
        label="화장실에서/샤워 후",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_5 = models.BooleanField(
        label="휴식시",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_6 = models.BooleanField(
        label="습관적 상황에서 (활력이 필요할 때/담배를 피우지 않음을 깨달을 때, 술/커피마실 때, 혼자 있거나 무언가 기다릴 때 등",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_7 = models.BooleanField(
        label="긍정적 상황 (친구나 가족과 함께 있을 때, 대화나 피로를 풀 때 등",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_8 = models.BooleanField(
        label="부정적 상황 (스트레스 받을 때, 일이 뜻대로 안될 때, 화날 때 등",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_9 = models.BooleanField(
        label="흡연자와 같이 있거나, TV의 배우 또는 주위 흡연자의 모습을 보았을 때",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_10 = models.BooleanField(
        label="흡연을 참기 힘들지 않음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_11 = models.StringField(
        label="기타",
        blank=True,
    )

    first_tobacco_of_the_day = models.IntegerField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 아침에 일어나서 얼마 만에 첫 일반담배(궐련)를 피우십니까?",
        choices=[
            [1, "5분 이내"],
            [2, "6분~30분 사이"],
            [3, "31분~1시간 사이"],
            [4, "1시간 이후"],
        ],
        widget=widgets.RadioSelect,
    )

    is_it_hard_to_resist_smoking_in_the_public = models.BooleanField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 금연구역(도서관, 극장, 병원 등)에서 일반담배(궐련)를 참기가 어렵습니까?",
        choices=[
            [1, "예"],
            [2, "아니오"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    when_is_tobacco_the_most_tasty = models.BooleanField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 하루 중 일반담배(궐련) 맛이 가장 좋은 때는 언제입니까?",
        choices=[
            [1, "예"],
            [2, "아니오"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    number_of_sticks_per_day_in_the_past = models.IntegerField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 하루에 보통 몇 개비나 피우십니까?",
        choices=[
            [1, "10개비 이하"],
            [2, "11~20개비"],
            [3, "21~30개비"],
            [4, "31개비 이상"],
        ],
        widget=widgets.RadioSelect,
    )

    is_morning_tobacco_more_tasty_than_the_rest = models.BooleanField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 아침에 일어나서 첫 몇 시간 동안 하루 중 다른 시간보다 더 자주 일반담배(궐련)를 피우십니까?",
        choices=[
            [1, "예"],
            [2, "아니오"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    sick_all_day_still_smoking = models.BooleanField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 몸이 아파 하루 종일 누워있을 때에도 일반담배(궐련)를 피우십니까?",
        choices=[
            [1, "예"],
            [2, "아니오"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    do_you_use_liquid_cigarette = models.IntegerField(
        label="귀하께서는 현재 액상형 전자담배(쥴, 탱크형 등)를 사용하십니까?",
        choices=[
            [1, "매일 사용"],
            [2, "가끔 사용"],
            [3, "과거엔 사용했으나, 현재는 사용하지 않음"],
            [4, "과거에도 , 현재에도 사용한 적 없음"],
        ],
        widget=widgets.RadioSelect,
    )

    liquid_cigarette_start_year = models.IntegerField(
        label="",
        choices=[
            [1, "11"],
            [2, "12"],
            [3, "13"],
            [4, "14"],
            [5, "15"],
            [6, "16"],
            [7, "17"],
            [8, "18"],
            [9, "19"],
            [10, "20"],
        ],
        blank=True,
    )

    liquid_cigarette_start_month = models.IntegerField(
        label="",
        choices=range(1,13),
        blank=True,
    )

    liquid_cigarette_end_year = models.IntegerField(
        label="",
        choices=[
            [1, "11"],
            [2, "12"],
            [3, "13"],
            [4, "14"],
            [5, "15"],
            [6, "16"],
            [7, "17"],
            [8, "18"],
            [9, "19"],
            [10, "20"],
        ],
        blank=True,
    )
    liquid_cigarette_end_month = models.IntegerField(
        label="",
        choices=range(1,13),
        blank=True,
    )

    most_recent_month_liquid_cigarette_use_days = models.IntegerField(
        label="최근 1달 간 액상형 전자담배(쥴, 탱크형 등) 사용일수",
        choices=range(1, 31),
        blank=True,
    )

    liquid_amount_of_liquid_cigarette_recent_week = models.IntegerField(
        label="",
        choices=range(101),
        blank=True,
    )

    liquid_cigarette_density = models.IntegerField(
        label="귀하가 현재 사용하는 또는 과거에 사용한 액상형 전자담배(쥴, 탱크형 등) 액상의 니코틴 농도(액상 1ml 기준 니코틴 함유량)는 얼마입니까? (1mg/ml=0.1%)",
        choices=[
            [1, "니코틴 없음"],
            [2, "1~6mg/ml"],
            [3, "7~12mg/ml"],
            [4, "13~18mg/ml"],
            [5, "19mg/ml 이상"],
            [6, "잘 모름"],
        ],
        widget=widgets.RadioSelect,
    )

    liquid_cigarette_hardest_to_resist_when_1 = models.BooleanField(
        label="아침에 일어나자마자",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_2 = models.BooleanField(
        label="잠들기 전",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_3 = models.BooleanField(
        label="식사 후",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_4 = models.BooleanField(
        label="화장실에서/샤워 후",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_5 = models.BooleanField(
        label="휴식시간",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_6 = models.BooleanField(
        label="습관적 상황에서 (활력이 필요할 때/전자담배를 사용하지 않음을 깨달을 때, 술/커피마실 때, 혼자 있거나 무언가 기다릴 때등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_7 = models.BooleanField(
        label = "긍정적 상황 (친구나 가족과 함께 있을 때, 대화나 피로를 풀 때 등)",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    liquid_cigarette_hardest_to_resist_when_8 = models.BooleanField(
        label = "부정적 상황 (스트레스 받을 때, 일이 뜻대로 안될 때, 화날 때 등)",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    liquid_cigarette_hardest_to_resist_when_9 = models.BooleanField(
        label = "흡연자와 같이 있거나, TV의 배우 또는 주위 흡연자의 모습을 보았을 때 ",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    liquid_cigarette_hardest_to_resist_when_10 = models.BooleanField(
        label = "사용을 참기 힘들지 않음",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    liquid_cigarette_hardest_to_resist_when_11 = models.StringField(
        label = "기타(직접입력:)",
        blank = True,
    )

    liquid_cigarette_first_in_the_day = models.IntegerField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 아침에 일어나서 얼마 만에 첫 액상형 전자담배(쥴, 탱크형 등)를 사용하십니까?",
        choices=[
            [1, "5분 이내"],
            [2, "6분~30분 사이"],
            [3, "31분~1시간 사이"],
            [4, "1시간 이후"],
        ],
        widget=widgets.RadioSelect,
    )

    is_it_hard_to_resist_smoking_liquid_cigarette_in_public = models.BooleanField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 금연구역(도서관, 극장, 병원 등)에서 액상형 전자담배(쥴, 탱크형 등)를 참기가 어렵습니까?",
        choices=[
            [1, "예"],
            [2, "아니오"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    when_is_the_liquid_cigarette_the_most_tasty = models.BooleanField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 하루 중 액상형 전자담배(쥴, 탱크형 등) 맛이 가장 좋은 때는 언제입니까?",
        choices=[
            [1, "아침 첫 사용시기"],
            [2, "그 외의 사용시기"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    liquid_cigarette_use_frequency_per_day = models.IntegerField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 하루에 보통 몇 번 사용하십니까?",
        choices = [
                  [1, "10회 이하"],
                  [2, "11~20회"],
                  [3, "21~30회"],
                  [4, "31회 이상"],
              ],
        widget = widgets.RadioSelect,
    )

    liquid_cigarette_morning_is_more_tasty_than_the_rest = models.BooleanField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 아침에 일어나서 첫 몇 시간 동안 하루 중 다른 시간보다 더 자주 액상형 전자담배(쥴, 탱크형 등)를 사용하십니까?",
        choices=[
            [1, "예"],
            [2, "아니오"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    liquid_cigarette_sick_all_day_still_smoking = models.BooleanField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 몸이 아파 하루 종일 누워있을 때에도 액상형 전자담배(쥴, 탱크형 등)를 사용하십니까?",
        choices=[
            [1, "예"],
            [2, "아니오"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    do_you_use_tobacco_type_e_cigarette = models.IntegerField(
        label="현재 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 사용하십니까?",
        choices=[
            [1, "매일 사용함"],
            [2, "가끔 사용함"],
            [3, "과거엔 사용했었으나, 현재는 사용하지 않음"],
            [4, "과거에도 , 현재에도 사용한 적 없음"],
        ],
        widget=widgets.RadioSelect,
    )

    tobacco_type_e_cigarette_start_year = models.IntegerField(
        label="",
        choices=[
            [1, "00"],
            [2, "01"],
            [3, "02"],
            [4, "03"],
            [5, "04"],
            [6, "05"],
            [7, "06"],
            [8, "07"],
            [9, "08"],
            [10, "09"],
            [11, "10"],
            [12, "11"],
            [13, "12"],
            [14, "13"],
            [15, "14"],
            [16, "15"],
            [17, "16"],
            [18, "17"],
            [19, "18"],
            [20, "19"],
            [21, "20"],
        ],
        blank=True,
    )
    tobacco_type_e_cigarette_start_month = models.IntegerField(
        label="",
        choices=range(1, 13),
        blank=True,
    )

    tobacco_type_e_cigarette_end_year = models.IntegerField(
        label="",
        choices=[
            [1, "00"],
            [2, "01"],
            [3, "02"],
            [4, "03"],
            [5, "04"],
            [6, "05"],
            [7, "06"],
            [8, "07"],
            [9, "08"],
            [10, "09"],
            [11, "10"],
            [12, "11"],
            [13, "12"],
            [14, "13"],
            [15, "14"],
            [16, "15"],
            [17, "16"],
            [18, "17"],
            [19, "18"],
            [20, "19"],
            [21, "20"],
        ],
        blank=True,
    )
    tobacco_type_e_cigarette_end_month = models.IntegerField(
        label="",
        choices=range(1, 13),
        blank=True,
    )

    within_recent_month_days_of_use_for_tobacco_type_e_cigarette = models.IntegerField(
        label="",
        choices=range(1, 31),
        blank=True,
    )

    tobacco_type_e_cigarette_avg_sticks_per_day = models.IntegerField(
        label="",
        choices=range(1, 101),
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_1 = models.BooleanField(
        label="아침에 일어나자마자",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_2 = models.BooleanField(
        label="잠들기 전",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_3 = models.BooleanField(
        label="식사 후",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_4 = models.BooleanField(
        label="화장실에서/샤워 후",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_5 = models.BooleanField(
        label="휴식시간",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_6 = models.BooleanField(
        label="습관적 상황에서 (활력이 필요할 때/전자담배를 사용하지 않음을 깨달을 때, 술/커피마실 때, 혼자 있거나 무언가 기다릴 때 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_7 = models.BooleanField(
        label="긍정적 상황 (친구나 가족과 함께 있을 때, 대화나 피로를 풀 때 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_8 = models.BooleanField(
        label="부정적 상황 (스트레스 받을 때, 일이 뜻대로 안될 때, 화날 때 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_9 = models.BooleanField(
        label="흡연자와 같이 있거나, TV의 배우 또는 주위 흡연자의 모습을 보았을 때",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_10 = models.BooleanField(
        label="사용을 참기 힘들지 않음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_11 = models.StringField(
        label="기타",
        blank=True,
    )

    tobacco_type_e_cigarette_first_in_the_day = models.IntegerField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 흡연자는 흡연당시 기준으로 작성) 아침에 일어나서 얼마 만에 첫 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 사용하십니까?",
        choices=[
            [1, "5분 이내"],
            [2, "6분~30분 사이"],
            [3, "31분~1시간 사이"],
            [4, "1시간 이후"],
        ],
        widget=widgets.RadioSelect,
    )

    tobacco_type_e_cigarette_hard_to_resist_in_public = models.BooleanField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 금연구역(도서관, 극장, 병원 등)에서 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 참기가 어렵습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    tobacco_type_e_cigarette_most_tasty_in_the_day = models.BooleanField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 하루 중 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 맛이 가장 좋은 때는 언제입니까?",
        choices=[
            [1, "아침 첫 사용 시기"],
            [2, "그 외의 사용 시기"],
        ],
        widget = widgets.RadioSelectHorizontal,
    )

    tobacco_type_e_cigarette_sticks_per_day = models.IntegerField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 하루에 보통 몇 개비를 사용하십니까?",
        choices=[
            [1, "10개비 이하"],
            [2, "11~20개비"],
            [3, "21~30개비"],
            [4, "31개비 이상"],
        ],
         widget = widgets.RadioSelect,
    )

    tobacco_type_e_cigarette_more_tasty_in_the_morning_than_the_rest = models.BooleanField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 아침에 일어나서 첫 몇 시간 동안 하루 중 다른 시간보다 더 자주 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 사용하십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    tobacco_type_e_cigarette_sick_all_day_still_smoking = models.BooleanField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 몸이 아파 하루 종일 누워있을 때에도 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 사용하십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_cessation_attempt_count = models.IntegerField(
        label="귀하께서는 금연 시도 경험이 있다고 답변하신 바 있습니다. 지금까지 금연 시도를 몇 번 정도 시도하셨습니까?",
        choices=[
            [1, "1회"],
            [2, "2회"],
            [3, "3회"],
            [4, "4회"],
            [5, "5회 이상"],
        ],
        widget=widgets.RadioSelect,
    )

    within_one_month_do_you_plan_to_quit_smoking = models.IntegerField(
        label="앞으로 1개월 안에 담배를 끊을 계획이 있습니까?",
        choices=[
            [1, "1개월내 금연할 계획이 있음"],
            [2, "6개월내 금연할 계획이 있음"],
            [3, "6개월내 아니지만 언젠가 금연생각 있음"],
            [4, "현재 전혀 금연 생각 없음"],
            [5, "현재 금연중임"],
        ],
        widget=widgets.RadioSelect,
    )

    within_past_five_days_last_time_to_use_nicotine_alternatives = models.IntegerField(
        label="최근 5일 동안 니코틴 패치, 니코틴 껌, 니코틴 사탕 등의 니코틴 대체용품을 마지막으로 사용한 때는 언제입니까?",
        choices=[
            [1, "오늘 사용"],
            [2, "1일 전 사용"],
            [3, "2일 전 사용"],
            [4, "3~5일전사용"],
            [5, "최근 5일 동안 사용하지 않음"],
            [6, "지금까지 사용해본 적 없음"],
        ],
        widget=widgets.RadioSelect,
    )
