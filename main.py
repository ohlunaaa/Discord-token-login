from selenium import webdriver
t = input("Token: ")
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://discord.com/login')
js = """
        function login(token) {
        setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
        location.reload();
        }, 2500);
        }   
        """
driver.execute_script(js + f'login("{t}")')
