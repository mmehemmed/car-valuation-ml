from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    page.goto("https://turbo.az/autos?q%5Bmake%5D%5B%5D=4")
    page.wait_for_selector(".products-i")
    
    # 2. Extract all listing links on this page
    # Links look like: "/autos/10482266-bmw-530"
    links = page.query_selector_all(".products-i__link")
    
    valid_urls = []
    for link in links:
        href = link.get_attribute("href")
        if href:
            full_url = "https://turbo.az" + href
            valid_urls.append(full_url)
            
    print(f"Found {len(valid_urls)} real, active car URLs:")
    print("Sucsessfully found the links")
        
    browser.close()

with open("links.txt", "a") as file:
    for item in valid_urls:
        file.write(f"{item}\n")
    print("Finished saving the links")