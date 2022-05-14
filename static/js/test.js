window.addEventListener('DOMContentLoaded', function(){
  $('[name=comic_name]').change(function() {
    // 選択されているvalue属性値を取り出す
    var val = $('[name=comic_name]').val();
    console.log(val);
    // 選択されている表示文字列を取り出す
    var txt = $('[name=comic_name] option:selected').text();
    console.log(txt);
  });
});