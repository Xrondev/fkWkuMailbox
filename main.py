import requests

url = "https://wku.edu.cn/cf-api/CF5d8c5acb13807/"

header = {
    'Accept': '*/*',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarys4WpPQhywiRCaiuS',
    'Referer': 'https://wku.edu.cn/xiaozhangxinxiang/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec - ch - ua - platform': '"Windows"',
    'X - Requested - With': 'XMLHttpRequest'
}

form_data = '''
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="_cf_verify"

52adbb7906
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="_wp_http_referer"

/xiaozhangxinxiang/
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="_cf_frm_id"

CF5d8c5acb13807
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="_cf_frm_ct"

1
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="cfajax"

CF5d8c5acb13807
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="_cf_cr_pst"

8758
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="web_site"


------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="fld_6433628"

其他
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="fld_3191505"

 
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="fld_5838398"; filename=""
Content-Type: application/octet-stream


------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="fld_5838398"

trupl63f08f2f54c5e
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="fld_9117347"

 
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="fld_7810285"

 
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="fld_5315043"

 
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="fld_3467807"

 
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="fld_236376"

click
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="fld_3634484"


------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="fld_9474691"


------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="fld_5898132"


------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="instance"

1
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="request"

https://wku.edu.cn/cf-api/CF5d8c5acb13807
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="formId"

CF5d8c5acb13807
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="postDisable"

0
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="target"

#caldera_notices_1
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="loadClass"

cf_processing
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="loadElement"

_parent
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="hiderows"

true
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="action"

cf_process_ajax_submit
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="cfajax"

CF5d8c5acb13807
------WebKitFormBoundarys4WpPQhywiRCaiuS
Content-Disposition: form-data; name="template"

#cfajax_CF5d8c5acb13807-tmpl
------WebKitFormBoundarys4WpPQhywiRCaiuS--
'''


req = requests.post(url, data=form_data.encode('utf-8'), headers=header)
print(req.status_code, req.content.decode())
