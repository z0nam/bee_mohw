"use strict";

var op_checker = function op_checker(radio_id, op_id) {
  var radio_tag = "#" + radio_id;
  var op_tag = "#" + op_id;
  var radio_parent = $(radio_tag).parent().parent().parent();

  var set_current_status = function set_current_status() {
    if ($(radio_tag).is(":checked")) {
      $(op_tag).show();
    } else {
      $(op_tag).hide();
    }
  };

  set_current_status();
  radio_parent.change(function () {
    set_current_status();
  });
};

var show_after = function show_after(id, seconds) {
  var tag = "#" + id;
  $(tag).delay(seconds * 1000).fadeIn();
};

var checkbox_hider = function checkbox_hider(checkbox_id, receiver_id) {
  var checkbox_tag = "#" + checkbox_id;
  var receiver_tag = "#" + receiver_id;
  $(checkbox_tag).change(function () {
    console.log(checkbox_tag + " changed");

    if ($(checkbox_tag).is(":checked")) {
      $(receiver_tag).val(0).hide();
    } else {
      $(receiver_tag).show();
    }
  });
};

var checkbox_shower = function checkbox_shower(checkbox_id, receiver_id) {
  var checkbox_tag = "#" + checkbox_id;
  var receiver_tag = "#" + receiver_id;
  $(checkbox_tag).change(function () {
    console.log(checkbox_tag + " changed");

    if ($(checkbox_tag).is(":checked")) {
      $(receiver_tag).show();
    } else {
      $(receiver_tag).hide();
    }
  });
};