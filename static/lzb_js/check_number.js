    /**
     * 限制输入2位小数。这里只能输入正数
     * @param {Object} Obj 输入框的this对象
	 * Demo
	 *   <input class="form-control" id="volume" name="volume"  placeholder="体积" type="text"  oninput="limit_Decimal_2(this)" required />
	 *
     */
    function limit_Decimal_2(obj) {
      if (isNaN(obj.value) && !/^\d$/.test(obj.value)) {
        obj.value = obj.value.slice(0, obj.value.length - 1)
      }
      if (!/^\d*\.{0,1}\d{0,1}$/.test(obj.value)) {
        obj.value = obj.value.replace(/\.\d{2,}$/, obj.value.substr(obj.value.indexOf("."), 3))
      }
    }
