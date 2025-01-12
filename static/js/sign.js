let sign = {
    'signIn':{
        "box":"signinbox",
        "head_txt":"Log in",
        "mail_txt":"email",
        "btn_txt":"Log in",
        "destination":"tosignup",
        "msg":"Not a member ? Sign up."
    },
    'signUp':{
        "box":"signupbox",
        "head_txt":"Create your account",
        "mail_txt":"email",
        "btn_txt":"Create account",
        "destination":"tosignin",
        "msg":"Already a member ? Sign in."
    }
};


//動態顯示填資料表格
function render_fillin(on_record_page=false){
    if(on_record_page===true){
        let navmenu = document.querySelector(".navmenu");
        let maincontainer = document.querySelector(".main-container");
        document.body.removeChild(navmenu);
        document.body.removeChild(maincontainer);
    }else{
        //移掉登入註冊匡
        let section2 = document.querySelector(".section-2");
        document.body.removeChild(section2);
    }

    let basic_information = document.createElement("div");
    basic_information.classList.add("basic-information");
    let welcome = document.createElement("div");
    welcome.setAttribute("id","welcome");
    const welcome_word1 = "Welcome！"
    const mybr = document.createElement('br');
    const welcome_word2 = "Please fill in personal information, we'll provide recommended diet plan for you later~"
    welcome.appendChild(document.createTextNode(welcome_word1));
    welcome.appendChild(mybr);
    welcome.appendChild(document.createTextNode(welcome_word2));
    basic_information.appendChild(welcome);
    let form_box = document.createElement("div");
    form_box.classList.add("form-box");
    let form = document.createElement("form");
    form.classList.add("form");
    let choose_gender = document.createElement("div");
    choose_gender.classList.add("choose-gender");
    let gender = document.createElement("span");
    gender.classList.add("describe");
    gender.classList.add("gender");
    gender.appendChild(document.createTextNode("Gender :"));
    let male = document.createElement("input");
    male.setAttribute("id","male");
    male.setAttribute("type","radio");
    male.setAttribute("name","gender");
    male.setAttribute("value","1");
    male.checked=true;
    let label_male = document.createElement("label");
    label_male.setAttribute("for","male");
    label_male.appendChild(document.createTextNode("male"));
    let female = document.createElement("input");
    female.setAttribute("id","female");
    female.setAttribute("type","radio");
    female.setAttribute("name","gender");
    female.setAttribute("value","0");
    let label_female = document.createElement("label");
    label_female.setAttribute("for","female");
    label_female.appendChild(document.createTextNode("female"));
    choose_gender.appendChild(gender);
    choose_gender.appendChild(male);
    choose_gender.appendChild(label_male);
    choose_gender.appendChild(female);
    choose_gender.appendChild(label_female);
    form.appendChild(choose_gender);
    let choose_age = document.createElement("div");
    choose_age.classList.add("choose-age");
    let age = document.createElement("span");
    age.classList.add("describe");
    age.classList.add("age");
    age.appendChild(document.createTextNode("Age :"));
    let age_input = document.createElement("input");
    age_input.setAttribute("id","age");
    age_input.setAttribute("type","text");
    age_input.setAttribute("name","age");
    age_input.setAttribute("placeholder","Age");
    choose_age.appendChild(age);
    choose_age.appendChild(age_input);
    form.appendChild(choose_age);
    let choose_height = document.createElement("div");
    choose_height.classList.add("choose-height");
    let height = document.createElement("span");
    height.classList.add("describe");
    height.classList.add("height");
    height.appendChild(document.createTextNode("Height :"));
    let height_input = document.createElement("input");
    height_input.setAttribute("id","height");
    height_input.setAttribute("type","text");
    height_input.setAttribute("name","height");
    height_input.setAttribute("placeholder","Height (cm)");
    choose_height.appendChild(height);
    choose_height.appendChild(height_input);
    form.appendChild(choose_height);
    let choose_weight = document.createElement("div");
    choose_weight.classList.add("choose-weight");
    let weight = document.createElement("span");
    weight.classList.add("describe");
    weight.classList.add("weight");
    weight.appendChild(document.createTextNode("Weight :"));
    let weight_input = document.createElement("input");
    weight_input.setAttribute("id","weight");
    weight_input.setAttribute("type","text");
    weight_input.setAttribute("name","weight");
    weight_input.setAttribute("placeholder","Weight (kg)");
    choose_weight.appendChild(weight);
    choose_weight.appendChild(weight_input);
    form.appendChild(choose_weight);
    let choose_activity = document.createElement("div");
    choose_activity.classList.add("choose-activity");
    let activity_level = document.createElement("h3");
    activity_level.classList.add("describe");
    activity_level.appendChild(document.createTextNode("Activity Level :"));
    let zero = document.createElement("div");
    zero.setAttribute("id","zero");
    let level1_input = document.createElement("input");
    level1_input.setAttribute("id","level1");
    level1_input.setAttribute("type","radio");
    level1_input.setAttribute("name","habit");
    level1_input.setAttribute("value","1");
    level1_input.checked=true;
    let label_level1 = document.createElement("label");
    label_level1.setAttribute("for","level1");
    label_level1.appendChild(document.createTextNode("sedentary (little/no exercise)"));
    zero.appendChild(level1_input);
    zero.appendChild(label_level1);
    let light = document.createElement("div");
    light.setAttribute("id","light");
    let level2_input = document.createElement("input");
    level2_input.setAttribute("id","level2");
    level2_input.setAttribute("type","radio");
    level2_input.setAttribute("name","habit");
    level2_input.setAttribute("value","2");
    let label_level2 = document.createElement("label");
    label_level2.setAttribute("for","level2");
    label_level2.appendChild(document.createTextNode("light activity (exercise 1~2 times/week)"));
    light.appendChild(level2_input);
    light.appendChild(label_level2);
    let moderate = document.createElement("div");
    moderate.setAttribute("id","moderate");
    let level3_input = document.createElement("input");
    level3_input.setAttribute("id","level3");
    level3_input.setAttribute("type","radio");
    level3_input.setAttribute("name","habit");
    level3_input.setAttribute("value","3");
    let label_level3 = document.createElement("label");
    label_level3.setAttribute("for","level3");
    label_level3.appendChild(document.createTextNode("moderate activity (exercise 3~4 times/week)"));
    moderate.appendChild(level3_input);
    moderate.appendChild(label_level3);
    let heavy = document.createElement("div");
    heavy.setAttribute("id","heavy");
    let level4_input = document.createElement("input");
    level4_input.setAttribute("id","level4");
    level4_input.setAttribute("type","radio");
    level4_input.setAttribute("name","habit");
    level4_input.setAttribute("value","4");
    let label_level4 = document.createElement("label");
    label_level4.setAttribute("for","level4");
    label_level4.appendChild(document.createTextNode("very active (exercise >5 times/week)"));
    heavy.appendChild(level4_input);
    heavy.appendChild(label_level4);
    choose_activity.appendChild(activity_level);
    choose_activity.appendChild(zero);
    choose_activity.appendChild(light);
    choose_activity.appendChild(moderate);
    choose_activity.appendChild(heavy);
    form.appendChild(choose_activity);
    //<div class="choose-target">
    let choose_target = document.createElement("div");
    choose_target.classList.add("choose-target");
    //<span class="describe target">Target :</span>
    let target = document.createElement("span");
    target.classList.add("describe");
    target.classList.add("target");
    target.appendChild(document.createTextNode("Target :"));
    //<input id="lose" type="radio" name="target" value="1">
    let lose_input = document.createElement("input");
    lose_input.setAttribute("id","lose");
    lose_input.setAttribute("type","radio");
    lose_input.setAttribute("name","target");
    lose_input.setAttribute("value","1");
    let label_lose = document.createElement("label");
    label_lose.setAttribute("for","lose");
    label_lose.appendChild(document.createTextNode("Lose weight"));
    //<input id="maintain" type="radio" name="target" value="2" checked>
    let maintain_input = document.createElement("input");
    maintain_input.setAttribute("id","maintain");
    maintain_input.setAttribute("type","radio");
    maintain_input.setAttribute("name","target");
    maintain_input.setAttribute("value","2");
    maintain_input.checked=true;
    let label_maintain = document.createElement("label");
    label_maintain.setAttribute("for","maintain");
    label_maintain.appendChild(document.createTextNode("Maintain"));
    //<input id="gain" type="radio" name="target" value="3">
    let gain_input = document.createElement("input");
    gain_input.setAttribute("id","gain");
    gain_input.setAttribute("type","radio");
    gain_input.setAttribute("name","target");
    gain_input.setAttribute("value","3");
    let label_gain = document.createElement("label");
    label_gain.setAttribute("for","gain");
    label_gain.appendChild(document.createTextNode("Gain weight"));
    choose_target.appendChild(target);
    choose_target.appendChild(lose_input);
    choose_target.appendChild(label_lose);
    choose_target.appendChild(maintain_input);
    choose_target.appendChild(label_maintain);
    choose_target.appendChild(gain_input);
    choose_target.appendChild(label_gain);
    form.appendChild(choose_target);
    //<div class="submit">Calculate</div>
    let submit = document.createElement("div");
    submit.classList.add("submit");
    submit.appendChild(document.createTextNode("Calculate"));
    //註冊按下calculate鈕事件
    submit.addEventListener("click",()=>{
        //先檢查表單資料都對不對&有沒有填
        let validate = validate_form();
        if(validate){
            let json_data = organize_form();
            submit_information(json_data);
        }
    });
    form.appendChild(submit);
    form_box.appendChild(form);
    basic_information.appendChild(form_box);
    //最後把basic-inofrmation放在section1後面
    if(on_record_page===false){
        let section1 = document.querySelector(".section-1");
        section1.after(basic_information);
    }else{
        // Create the main section element
        const section = document.createElement('div');
        section.className = 'section-1';
        // Create the nav element
        const nav = document.createElement('div');
        nav.className = 'nav';
        // Create the header element
        const header = document.createElement('div');
        header.className = 'header-1';
        // Create the span element with text
        const span = document.createElement('span');
        span.textContent = 'Macros Eat';
        // Create the image element
        const img = document.createElement('img');
        img.className = 'logo';
        img.src = 'data:image/png;base64,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';
        header.appendChild(span);
        header.appendChild(img);
        nav.appendChild(header);
        section.appendChild(nav);
        document.body.appendChild(section);
        let section1 = document.querySelector(".section-1");
        section1.after(basic_information);
    }
}



//show登入註冊訊息
function showMessage(msg,flag,signup_result){
    if(flag){
        let button = document.getElementById("signbtn");
        let signin_content = document.querySelector(".content");
        let previous_message_div = document.querySelector(".message");
        if (previous_message_div){
            signin_content.removeChild(previous_message_div);
        };
        let fail_div  = document.createElement("div");
        fail_div.appendChild(document.createTextNode(msg));
        fail_div.classList.add('message');
        signin_content.style.height = "270px";
        button.after(fail_div);    
    }else{
        if(signup_result){
            let button = document.getElementById("signbtn");
            let signup_content = document.querySelector(".content");
            let previous_message_div = document.querySelector(".message");
            if (previous_message_div){
                signup_content.removeChild(previous_message_div);
            };
            let succeed_div  = document.createElement("div");
            succeed_div.appendChild(document.createTextNode(msg));
            succeed_div.classList.add('message');
            signup_content.style.height = "325px";
            button.after(succeed_div);
        }else{
            let button = document.getElementById("signbtn");
            let signup_content = document.querySelector(".content");
            let previous_message_div = document.querySelector(".message");
            if (previous_message_div){
                signup_content.removeChild(previous_message_div);
            };
            let fail_div  = document.createElement("div");
            fail_div.appendChild(document.createTextNode(msg));
            fail_div.classList.add('message');
            signup_content.style.height = "325px";
            button.after(fail_div);    
        };          
    };    
};


//切換顯示註冊會員<->登入
function switchBox(flag){
    let section2 = document.querySelector(".section-2")
    while(section2.firstElementChild){
        section2.removeChild(section2.firstElementChild)
    }
    //flag true代表有帳戶,false沒有帳戶
    if(flag){
        showBox(sign.signIn, true);
    }else{
        showBox(sign.signUp, false);
    };
};



//處理送出註冊資訊
async function sendAuthSignUp(data){
    try{
        let response = await fetch('/authen/signup/',{
                                     method: 'post',
                                     body: data,
                                     headers: { 'Content-Type': 'application/json'}
                                    });
        let result = await response.json();
        if(response.status === 201){
                showMessage("Sign up completed. Please sign in.", false, true);
        }else if(response.status === 400){ //1.email重複 2.註冊信箱或密碼格式錯誤
            showMessage(result.message,false,false);
            //清空信箱和密碼輸入框
            let mail_input = document.querySelector('.email');
            let pass_input = document.querySelector('.pass');
            mail_input.value='';
            pass_input.value='';
        }else if(response.status === 500){ //如果是500,代表伺服器(資料庫)內部錯誤
            showMessage(result.message, false, false);
        };
    }catch(message){
        console.log(`${message}`)
        throw Error('Signup endpoint fetching fail')
    }
}


//處理送出登入資訊
async function sendAuthSignIn(data){
    try{
        let response = await fetch('/authen/signin/',{
                                     method: 'post',
                                     body: data,
                                     headers: { 'Content-Type': 'application/json'}
                                        });
        let result = await response.json();
        if(response.ok){  //200情況下
                if(result["initial"] === true){ //表示還沒填寫資料頁面,動態 render填寫資料頁面
                    render_fillin();
                }else{ //表示有填寫過資料
                    window.location.href="/record/"
                }
        }else if(response.status === 400){ //代表1.密碼錯誤 2.沒有此信箱會員
                showMessage(result.message,true,null)
                let mail_input = document.querySelector('.email');
                let pass_input = document.querySelector('.pass');
                mail_input.value='';
                pass_input.value='';
        }else if(response.status === 500){ //如果是500,代表伺服器(資料庫)內部錯誤
                showMessage(result.message,true,null)
        };
    }catch(message){
        console.log(`${message}`)
        throw Error('Fetching was not ok!!.')
    }
}


//處理註冊事件
function handleSignUp(){
    let email = document.querySelector('.email').value;
    let password = document.querySelector('.pass').value;
    let name = document.querySelector('.name').value;
    let identity = document.getElementsByName('identity')[0].value;
    //前端驗證確實輸入或輸入正不正確
    if ((!name||!email) || (!password) || (identity==="0")){
        showMessage('Please fill in valid information',false,false);
    }else{
        let emailRegex = /^(?!\.{1,2})(?![^\.]*\.{2})(?!.*\.{2}@)(?=[a-zA-Z0-9\.!#\$%&\'\*\+\/=?\^_{\|}~-]+@{1}(?:[A-Za-z\d]+\.{1})+[a-zA-Z]+$)(?!.*@{2,}).*/g;
        let passwordRegex = /^(?=\w{8,16}$)(?=(?:[^A-Z]*[A-Z]){3})(?=[^a-z]*[a-z])(?=[^\d]*\d).*/g;
        //檢查看格式正不正確
        //if(emailRegex.test(email)&&passwordRegex.test(password)){
        if(emailRegex.test(email)){
            if(Number(identity)===1){
                let data = {  //註冊資訊
                    "name":name,
                    "email":email,
                    "password":password,
                    "identity":"general_user"
                }
                let req = JSON.stringify(data); //將註冊資料轉成json格式
                sendAuthSignUp(req);
            }else if (Number(identity)===2){
                let data = {  //註冊資訊
                    "name":name,
                    "email":email,
                    "password":password,
                    "identity":"nutritionist"
                }
                let req = JSON.stringify(data); //將註冊資料轉成json格式
                sendAuthSignUp(req);
            }
        }else{
            let button = document.getElementById("signbtn");
            let signup_content = document.querySelector(".content");
            let previous_message_div = document.querySelector(".message");
            if (previous_message_div){
                signup_content.removeChild(previous_message_div);
            };
            let fail_div  = document.createElement("div");
            let span = document.createElement("span");
            span.appendChild(document.createTextNode("Email is not correct."));
            fail_div.appendChild(span);
            fail_div.classList.add('message');
            signup_content.style.height = "410px";
            button.after(fail_div);
            //清空信箱和密碼輸入框
            let mail_input = document.querySelector('.email');
            mail_input.value='';
        };
    };
}


//處理登入事件
function handleSignIn(){
    let email = document.querySelector('.email').value;
    let password = document.querySelector('.pass').value;
    let identity = document.getElementsByName('identity')[0].value;
    if (!email || !password || (identity==='0')){
        showMessage('Please fill in valid information',true,null)
    }else{
        let data = {
            'email':email,
            'password':password,
            'identity':Number(identity)
        }
        let req = JSON.stringify(data); //轉成json格式
        sendAuthSignIn(req);
    }
}

//處理登出事件
async function handleSignOut(){
    try{
        let response = await fetch('/authen/signout/',{method: 'delete'});
        if(response.ok){ //200情況下
               //let identity = document.getElementById('user-email').getAttribute("identity")
               //if(identity==="2"){
               //    nutri_socket.emit("signout_disconnect");
               //}else{
               //    user_socket.emit("signout_disconnect");
               //}
        }
    }catch(message){
        console.log(`${message}`)
        throw Error('Fetching was not ok!!.')
    }
}


//show出登入/註冊框
function showBox(obj,flag){ //flag true代表有帳戶,false沒有帳戶
    let section2 = document.querySelector(".section-2");
    let sign_box = document.createElement("div");
    sign_box.className=obj.box //"signinbox signupbox";
    let sign_content = document.createElement("div");
    sign_content.className = "content";
    if(flag){
        sign_content.style.height="250px";
    }else{
        sign_content.style.height="307px";
    }
    let head = document.createElement("div");
    head.className = "head";
    let head_text = document.createTextNode(obj.head_txt);
    head.appendChild(head_text);
    sign_content.appendChild(head);
    //判斷是登入還是註冊(登入true,註冊false),如果是false要新增一欄"輸入姓名"
    if(!flag){
        let input_name = document.createElement("input");
        input_name.className = "name";
        input_name.setAttribute("placeholder","username");
        input_name.setAttribute("type","text");
        sign_content.appendChild(input_name);
    }
    //信箱輸入框
    let input_mail = document.createElement("input");
    input_mail.className = "email";
    input_mail.setAttribute("placeholder",obj.mail_txt);
    input_mail.setAttribute("type","text");
    //test account
    if(flag){
        input_mail.value = "test@gmail.com";
    };
    sign_content.appendChild(input_mail);
    //密碼輸入框
    let input_pass = document.createElement("input");
    input_pass.className = "pass";
    input_pass.setAttribute("placeholder","password");
    input_pass.setAttribute("type","password");
    sign_content.appendChild(input_pass);
    //test account
    if(flag){
        input_pass.value = "wayne123WAYNE";
    };
    //身份選擇匡
    let select = document.createElement("select");
    select.setAttribute("name",'identity');
    let option0 = document.createElement("option");
    option0.setAttribute("value",'0');
    option0.appendChild(document.createTextNode("Choose your identity"));
    let option1 = document.createElement("option");
    option1.setAttribute("value",'1');
    option1.appendChild(document.createTextNode("General user"))
    let option2 = document.createElement("option");
    option2.setAttribute("value",'2');
    option2.appendChild(document.createTextNode("Nutritionist"))
    select.appendChild(option0);
    select.appendChild(option1);
    select.appendChild(option2);
    //test account
    if(flag){
        select.value = "1";
    };
    sign_content.appendChild(select);
    //登入,註冊鈕
    let button = document.createElement("div");
    button.setAttribute("id","signbtn");
    let button_text = document.createTextNode(obj.btn_txt);
    button.appendChild(button_text);
    //不管是登入或註冊鈕,在創造出來的時候,就要加上eventlistener,目的是送出ajax到後端驗證的路由
    if(flag){
        button.addEventListener('click', function(){handleSignIn()})
    }else{
        button.addEventListener('click', function(){handleSignUp()})
    };
    sign_content.appendChild(button);
    //還沒有帳戶or已經有帳戶？
    let goto = document.createElement("div");
    goto.className = obj.destination;
    let goto_text = document.createTextNode(obj.msg);
    goto.appendChild(goto_text);
     //按下去換框框
    goto.addEventListener("click",function(){
                          switchBox(!flag)
                        });
    sign_content.appendChild(goto);
    //將主內容放入框框裡
    sign_box.append(sign_content);
    //如果是true,要多一個login with google
    if(flag){
        let google_signbox = document.createElement("div");
        google_signbox.classList.add("google-signbox");
        let google_btn = document.createElement("div");
        google_btn.classList.add("google-btn");
        let a = document.createElement("a");
        a.setAttribute("href","/login/google");
        let img = new Image();
        img.src = "https://d2fbjpv4bzz3d2.cloudfront.net/google.png";
        img.id = "google";
        let btn_text = document.createElement("div");
        btn_text.classList.add("google-btn-text");
        btn_text.appendChild(document.createTextNode("Continue with google"));
        a.appendChild(img);
        a.appendChild(btn_text);
        google_btn.appendChild(a);
        google_signbox.appendChild(google_btn);
        sign_box.append(google_signbox);
    };
    section2.appendChild(sign_box);
}


async function renderRecordCheck(){
    // 拿使用者資料，判斷是否有填過初始資料
    // 如果沒填過就要動態render初始資料表格
    // 有填過就可以 render紀錄頁面
    try{
        let response = await fetch('/authen/user/',{method: 'get'});
        let result = await response.json();
        if(response.ok && result.data["identity"]===1 && result.data["initial"]===false){
                // 有填過資料了可以顯示record頁面
                render_record(result.data);
                //}else if(window.location.pathname==='/helper'){
                //   connect_socket(1);
                //}
        }else if(response.ok && result.data["identity"]===1 && result.data["initial"]===true){ //代表登入後跳掉沒有填表單
            // 表示還沒填過
            render_fillin(on_record_page=true) //顯示表單;
        }else if (response.status === 403){
            console.log('cookie已失效,請重新登入');
            window.location.href = '/';
        }
        // 以下先不用管
        //}else if(response.ok && result.data["identity"]===2){ //代表是營養師,直接導到諮詢頁面
        //    if(window.location.pathname==='/helper'){
        //        connect_socket(2);
        //        handle_notification();
        //    }else{
        //        window.location.href="/helper";
        //    }
        //}else{
        //    window.location.replace('/') //導回首頁
        //};
    }catch(message){
        console.log(`${message}`)
        throw Error('Fetching was not ok!!.')
    };
};


function init_sign(){
    if (window.location.pathname ==='/'){
        let goto_signup = document.querySelector(".tosignup");
        goto_signup.addEventListener("click", ()=>{
            switchBox(false)
        });
        let signin_button = document.getElementById("signbtn");
        signin_button.addEventListener("click", function(){handleSignIn()});
        //for interview test account
        let identity = document.getElementsByName("identity")[0];
        identity.value = "1";
        let email = document.querySelector(".email");
        email.value = "wayne@gmail.com";
        let pwd = document.querySelector(".pass");
        pwd.value = "123";
    }else if (window.location.pathname ==='/record/'){
        // 準備 render 記錄頁面，要先檢查有沒有填過初始資料
        renderRecordCheck();
    }
}

window.addEventListener('load', init_sign);
