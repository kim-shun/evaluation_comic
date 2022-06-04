window.addEventListener('DOMContentLoaded', function(){
  function undisplay() {
    var free_area = document.getElementById("free_comic_area");
    free_area.style.display = "none";
  }
  $('[name=comic_name]').change(function() {
    // 選択されているvalue属性値を取り出す
    var val = $('[name=comic_name]').val();
    console.log(val);
    // 選択されている表示文字列を取り出す
    var txt = $('[name=comic_name] option:selected').text();
    console.log(txt);
  });

  $('#comic_name').on('change', function(){
    // テキストを取得(例：北海道)
    var area = $(this).children(':selected').text();
      if(area == '自由入力'){
        // 表示する
        $(this).next().slideToggle(500)
        // $(this).removeClass('hide');
      }
    });
  });

  $('.select').on('change', function(){
    // テキストを取得(例：北海道)
    var area = $(this).children(':selected').text();
  
    $('.area').each(function(){
      // 全て非表示にする(初期化)
      $(this).addClass('hide');
  
      // '全て'が選択されていれば
      if(area == '全て'){
        // 表示する
        $(this).removeClass('hide');
  
      // テキスト(例：北海道)が一致していれば
      }else if($(this).html().match(area)){
        // 表示する
        $(this).removeClass('hide');
      }
    });
  });
});