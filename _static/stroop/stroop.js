

class StroopTestItem {
    constructor(displayed_character, displayed_color_str, correct_color_str) {
        this.displayed_character = displayed_character;
        this.displayed_color_str = displayed_color_str;
        this.correct_color_str = correct_color_str;
    }
}

//  항목: 시간테이블, 경과시간, 라운드넘버, 피리오드, 표시문자, 표시색깔, 오답횟수 (0=바로정답, >0: 오답존재)

class StroopItem {
    constructor(
        timetable,
        elapsed_time,
        round_number,
        current_period,
        displayed_character,
        correct_color_str,
        number_of_errors
    ){
        this.timetable = timetable;
        this.elapsed_time = elapsed_time;
        this.round_number = round_number;
        this.current_period = current_period;
        this.displayed_color_str = displayed_character;
        this.correct_color_str = correct_color_str;
        this.number_of_errors = number_of_errors;
    };
}

// 항목: 시간테이블, 라운드넘버, 피리오드, 표시문자, 표시색깔, 정답, 클릭한색깔, 정답/오답여부
class StroopEvent {
    constructor(current_time,
               elapsed_time,
               round_number,
               current_period,
               displayed_character,
               displayed_color_str,
               correct_color_str,
               clicked_color_str,
               is_correct_answer){
        this.current_time = current_time;
        this.elapsed_time = elapsed_time;
        this.round_number = round_number;
        this.current_period = current_period;
        this.displayed_character = displayed_character;
        this.displayed_color_str = displayed_color_str;
        this.correct_color_str = correct_color_str;
        this.clicked_color_str = clicked_color_str;
        this.is_correct_answer = is_correct_answer;
    }
}

class Timer {
    constructor() {
       this.start_time = new Date().getTime();
    };

    start(){
        this.start_time = new Date().getTime();
    };

    get_elapsed(){
        return new Date().getTime() - this.start_time;
    };
};

let current_period = 1;
console.log("current_period set to 1");
const last_period = correct_answers.length;
let timer;

/**
 *  stroop_event_table: 클릭시마다 모든 이벤트 기록 (오답, 정답 여부 로그용) 많이 틀리면 총 피리오드수가 길어짐
 *      항목: 시간테이블, 경과시간, 라운드넘버, 피리오드, 표시문자, 표시색깔, 정답, 클릭한색깔, 정답/오답여부
 *  stroop_item_table: 문제 테이블. 출제된 문제들의 Object 기록
 *      항목: 라운드넘버, 피리오드, 표시문자, 표시색깔, 정답
 *  stroop_table: 피리오드, 걸린시간, 오답 있었는지 여부 기록. 총 피리오드수만큼만 기록됨.
 *      항목: 시간테이블, 경과시간, 라운드넘버, 피리오드, 정답, 오답횟수 (0=바로정답, >0: 오답존재)
 *
 * @type {*[]}
 */

let stroop_event_table = [];
let stroop_item_table = [];
let stroop_table = [];

for (i=0; i<correct_answers.length; i++){
    let displayed_color_str_to_add = color_strs[displayed_colors[i]];
    let correct_color_str = color_strs[correct_answers[i]];
    stroop_item_table.push(new StroopTestItem(
        displayed_characters[i],
        displayed_color_str_to_add,
        correct_color_str));
}

let num_wrong_answers_in_period = 0;
let total_num_wrong_answers = 0;

$(document).ready(function(){
    begin();
});

$(document).on('click', 'button', function(e){
    chosen_color_str = $(this).text().trim();
    console.log("button clicked with color: "+chosen_color_str);
    // alert("button clicked with color: "+chosen_color_str+"and correct color: "+color_strs[correct_answer]);
    correct_color_str = color_strs[correct_answer]
    displayed_color_str = color_strs[displayed_color]

    let is_correct;
    if(chosen_color_str == correct_color_str){
        is_correct = true;
    }else{
        is_correct = false;
    }

    stroop_event_table.push(new StroopEvent(
        new Date().getTime(),
        timer.get_elapsed(),
        round_number,
        current_period,
        displayed_character,
        displayed_color_str,
        correct_color_str,
        chosen_color_str,
        is_correct
    ));



    if (chosen_color_str == correct_color_str){
        mark_right();
        stroop_table.push(new StroopItem(
            new Date().getTime(),
            timer.get_elapsed(),
            round_number,
            current_period,
            displayed_character,
            correct_color_str,
            num_wrong_answers_in_period
        ));
        if(is_last_period()){
            current_period++;
            hide_marks();
            display_next_stage_alert();
            return;
        }
        clear_screen();
        prepare_next_period();
    }
    else{
        mark_wrong();
        return;
    }
});

const begin = () => {
    load_current_test();
    wait_for_answer();
};


const load_current_test = () => {
    num_wrong_answers_in_period = 0;
    if (was_last_period_end()){
        display_next_stage_alert();
        return;
    }

    correct_answer = correct_answers[current_period - 1];
    displayed_character = displayed_characters[current_period - 1];
    displayed_color = displayed_colors[current_period - 1];
    displayed_color_code = displayed_color_codes[current_period - 1];

    timer = new Timer();
    $('html').fadeIn(0);

    $("#keyword").html(displayed_character.toString()).css('color', displayed_color_code.toString())
};


const wait_for_answer = () => {
    // wait for touch or click; do nothing.
};

const was_last_period_end = () => {
    return current_period > last_period;
};

const is_last_period = () => {
    return current_period >= last_period;
};

const mark_wrong = () => {
    num_wrong_answers_in_period++;
    total_num_wrong_answers++;
    $("#wrong_answer_mark").show().fadeOut(100);
};

const mark_right = () => { //어떻게 해도 동그라미가 보이지 않는다. 새로 로드하면서 겹쳐지는 것 같은데 중요한 기능은 아니므로 일단 생략함.
    $("#right_answer_mark").show().fadeOut(100);
    // setTimeout(function(){},100);
};

const display_next_stage_alert = () => {
    alert("수고하셨습니다! 다음 단계로 진행해주시기 바랍니다. ");
    save_and_exit();
};

const save_and_exit = () => {
    const stroop_event_json = JSON.stringify(stroop_event_table);
    const stroop_item_json = JSON.stringify(stroop_item_table);
    const stroop_json = JSON.stringify(stroop_table);

    $("#stroop_event_table").val(stroop_event_json);
    $("#stroop_item_table").val(stroop_item_json);
    $("#stroop_table").val(stroop_json);

    if(round_number == 1){
        $("#c_time").val(timer.get_elapsed());
        $("#c_error").val(total_num_wrong_answers);
        $("#c_item_size").val(last_period);
    }else if(round_number == 2){
        $("#w_time").val(timer.get_elapsed());
        $("#w_error").val(total_num_wrong_answers);
        $("#w_item_size").val(last_period);
    }else if(round_number == 3){
        $("#cw_time").val(timer.get_elapsed());
        $("#cw_error").val(total_num_wrong_answers);
        $("#cw_item_size").val(last_period);
    }

    $("#form").submit();
};

const hide_marks = () => {
    $(".answer_mark").hide();
};

const clear_screen = () => {
    hide_marks();
    $("html").fadeOut(100);
};

const prepare_next_period = () => {
    current_period++;
    begin();
};
