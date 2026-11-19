screen_helper = """ 
ScreenManager:
    MenuScreen:
    ProfileScreen:
    ProductsScreen:
    ContactsScreen:
    UploadScreen:


<MenuScreen>:
    name: 'menu'
    MDLabel:  
        text: 'Screen Menu'
        halign: 'center'

    MDRectangleFlatButton:  
        text: 'Profile'
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
        on_press: root.manager.current = 'profile'

    MDRectangleFlatButton:  
        text: 'Upload'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        on_press: root.manager.current = 'upload'

    MDRectangleFlatButton:  
        text: 'Products'
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        on_press: root.manager.current = 'products'

    MDRectangleFlatButton:  
        text: 'Contacts'
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        on_press: root.manager.current = 'contacts'

    MDRectangleFlatButton:  
        text: 'Upload'
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        on_press: root.manager.current = 'upload'             

<ProfileScreen>:
    name: 'profile'
    MDLabel:  
        text: 'Screen Profile'
        halign: 'center'

    MDRectangleFlatButton:  
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu' 

<ProductsScreen>:
    name: 'products'
    MDLabel:  
        text: 'Screen Products'
        halign: 'center'

    MDRectangleFlatButton:  
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu' 

<ContactsScreen>:
    name: 'contacts'
    MDLabel:  
        text: 'Screen Contacts'
        halign: 'center'

    MDRectangleFlatButton:  
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu' 

<UploadScreen>:
    name: 'upload'
    MDLabel:  
        text: 'Screen Upload'
        halign: 'center'

    MDRectangleFlatButton:  
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'                               

"""