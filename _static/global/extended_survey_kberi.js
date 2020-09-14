const op_checker = (radio_id, op_id) => {
    let radio_tag = "#"+radio_id;
    let op_tag = "#"+op_id;
    let radio_parent = $(radio_tag).parent().parent().parent();
    const set_current_status = () => {
        if($(radio_tag).is(":checked")){
            $(op_tag).show();
        }else{
            $(op_tag).hide();
        }
    };
    set_current_status()
    radio_parent.change(
        function(){
            set_current_status()
        }
    )
};

const show_after = (id, seconds) => {
    const tag = "#"+id;
    $(tag).delay(seconds*1000).fadeIn()
}

const checkbox_hider = (checkbox_id, receiver_id) => {
    let checkbox_tag = "#"+checkbox_id;
    let receiver_tag = "#"+receiver_id;
    $(checkbox_tag).change(
        function(){
            console.log(checkbox_tag+" changed");
            if($(checkbox_tag).is(":checked")) {
                $(receiver_tag).val(0).hide()
            }else{
                $(receiver_tag).show()
            }
        }
    )
}

const checkbox_shower = (checkbox_id, receiver_id) => {
    let checkbox_tag = "#"+checkbox_id;
    let receiver_tag = "#"+receiver_id;
    $(checkbox_tag).change(
        function(){
            console.log(checkbox_tag+" changed");
            if($(checkbox_tag).is(":checked")) {
                $(receiver_tag).show()
            }else{
                $(receiver_tag).hide()
            }
        }
    )
}