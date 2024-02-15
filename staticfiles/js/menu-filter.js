document.getElementById('vegan-only').addEventListener('change', function() {
  let isChecked = this.checked;
  let veganItems = document.querySelectorAll('.vegan');

  veganItems.forEach(function(item) {
    if (isChecked) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  });
});