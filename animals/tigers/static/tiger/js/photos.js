var PhotoScroll = new Class({
    initialize:function(config, leftButton, rightButton, showFunction, count, className){
        this.photos = $('photos');
        this.className = className;
        // Destroy all photos
        this.photos.getElements('li').each(function(item){item.destroy()});

        // Initial configs
        this.conf = config;
        this.count = count || 7;
        this.leftButton = $(leftButton);
        this.rightButton = $(rightButton);
        this.show = showFunction;
        this.activePhoto = null;
        this.leftButton.addEvent('click', this.leftArrow.bind(this));
        this.rightButton.addEvent('click', this.rightArrow.bind(this));
        this.currentIndex = 0;

        this.drawPhotos();
        if (this.conf.length > this.count)
            this.rightButton.removeClass('hide');
        this.move(0)
    },
    leftArrow:function(e){
        e.stop();
        this.move(-1);
    },
    rightArrow:function(e){
        e.stop();
        this.move(1);
    },
    drawPhotos:function(){
        for (var i=0; i < this.count; i++) {
            var index = i+this.currentIndex;
            if (this.conf.length < index + 1)
                return
            var img = this.conf[index];
            var imgTag = new Element('img', {
                'src':img.preview,
                'alt':i+this.currentIndex,
                'title':img.photo});
            var aTag = new Element('a', {
                'href':img.photo,
                'rel':'milkbox[gal]',
                'title':img.title
            });
            if (this.show)
                aTag.addEvent('click', this.show.bind(this));
            var liTag = new Element('li', {'class':this.className});
            imgTag.inject(aTag);
            aTag.inject(liTag);
            liTag.inject(this.photos);
        }
    },
    move:function(position){
        if (this.conf.length < this.count ||
            this.conf.length - (this.currentIndex + position) < this.count ||
            this.currentIndex + position < 0 )
            return;
        this.currentIndex = this.currentIndex + position;
        // Destroy all photos
        this.photos.getElements('li').each(function(item){item.destroy()});
        this.drawPhotos()
        if (this.currentIndex > 0) {
            if ($('nleft'))
                $('nleft').setProperty('text', this.currentIndex);
            $(this.leftButton).removeClass('hide');
        } else {
            $(this.leftButton).addClass('hide');
            if ($('nleft'))
                $('nleft').setProperty('text', '');
        }
        var rightRested = this.conf.length - this.currentIndex - this.count;
        if (rightRested > 0) {
            if ($('nright'))
                $('nright').setProperty('text', rightRested);
            $(this.rightButton).removeClass('hide');
        } else {
            $(this.rightButton).addClass('hide');
            if ($('nright'))
                $('nright').setProperty('text', '');
        }
    }
});

var SideBlockPhotos = new Class({
    initialize:function(config, leftButton, rightButton, showFunction, count){
        this.photos = $('photos-preview');
        // Destroy all photos
        this.photos.getElements('a').each(function(item){item.destroy()});

        // Initial configs
        this.conf = config;
        this.count = count || 8;
        this.leftButton = $(leftButton);
        this.rightButton = $(rightButton);
        this.show = showFunction;
        this.activePhoto = null;
        this.leftButton.addEvent('click', this.leftArrow.bind(this));
        this.rightButton.addEvent('click', this.rightArrow.bind(this));
        this.currentIndex = 0;

        this.drawPhotos();
        if (this.conf.length > this.count)
            this.rightButton.removeClass('hide');
        this.move(0)
    },
    leftArrow:function(e){
        e.stop();
        this.move(-1);
    },
    rightArrow:function(e){
        e.stop();
        this.move(1);
    },
    drawPhotos:function(){
        for (var i=0; i < this.count; i++) {
            var index = i+this.currentIndex;
            if (this.conf.length < index + 1)
                return
            var img = this.conf[index];
            var imgTag = new Element('img', {
                'src':img.preview,
                'alt':i+this.currentIndex,
                'title':img.photo});
            var aTag = new Element('a', {
                'href':img.photo,
                'rel':'milkbox[gal]',
                'title':img.title
            });
            if (this.show)
                aTag.addEvent('click', this.show.bind(this));
            imgTag.inject(aTag);
            aTag.inject(this.photos);
        }
    },
    move:function(position){
        if (this.conf.length < this.count ||
            this.conf.length - (this.currentIndex + position) < this.count ||
            this.currentIndex + position < 0 )
            return;
        this.currentIndex = this.currentIndex + position;
        // Destroy all photos
        this.photos.getElements('a').each(function(item){item.destroy()});
        this.drawPhotos()
        if (this.currentIndex > 0) {
            $(this.leftButton).removeClass('hide');
        } else {
            $(this.leftButton).addClass('hide');
        }
        var rightRested = this.conf.length - this.currentIndex - this.count;
        if (rightRested > 0) {
            $(this.rightButton).removeClass('hide');
        } else {
            $(this.rightButton).addClass('hide');
        }
    }
});



var VideoPopup = function (kwargs) {
    this.overlay = new Element('div', { 'id':'video-overlay','styles':{ 'opacity':'0','visibility':'visible' }}).inject($(document.body));
    this.overlay.addEvent('click', function(e){
        e.stop();
        this.disappear();
    }.bind(this));
    this.center = new Element('div', {'id':'video-center', 'styles':{'width':kwargs.width,'height':kwargs.height,'marginLeft':-(kwargs.width/2),'opacity':0}}).inject($(document.body));
    this.image = new Element('div', {'id':'video-container', style:'height: 305px; width: 350px;'}).inject(this.center);
    var closeContainer = new Element('div', {'class':'closeButton','style':'font-size:10px; position:absolute; top:10px; right:0px;}'}).inject(this.center);
    var flagContainer = new Element('div', {'style':'position:absolute; top:0; right:0; width:4px; height:118px;'}).inject(this.center);
    var flag = new Element('img').inject(flagContainer);
    flag.set('src','/patron/static/img/flag.gif');
    this.bottom = new Element('div',{'id':'mbBottom', 'styles':{width:kwargs.width}}).inject(this.center).setStyle('visibility','visible');
    this.navigation = new Element('div',{'id':'mbNavigation'}).setStyle('visibility','hidden');
    desc = new Element('div',{"class":"desc"});
    this.date = new Element('div',{"class":"date"}).inject(desc);
    this.description = new Element('h6').inject(desc);
    this.bottom.adopt(this.navigation,desc);
    this.close = new Element('a',{'id':'mbCloseLink'}).inject(closeContainer);
    this.close.addEvent('click', function(e) {
        this.disappear();
    }.bind(this));
    texts = new Element('div').inject(this.close);
    var container = kwargs.container || $(document.body);
    $$(container).adopt(this.overlay);
    $$(container).adopt(this.center);
    this.render = function (player, title, date) {
        this.image.innerHTML = player;
        this.description.innerHTML = title;
        this.date.innerHTML = date;
        this.overlay.setStyle('top', '-168px');
        this.overlay.setStyle('height', '1000px');
        this.overlay.tween('opacity', 0.7);
        this.center.setStyle('visibility', 'visible');
        this.center.tween('opacity', 1);
    };
    this.disappear = function() {
        this.center.setStyle('visibility', 'hidden');
        this.center.setStyle('opacity', 0);
        this.image.innerHTML = '';
        this.overlay.setStyle('opacity', 0);
        this.overlay.setStyle('top', '0');
        this.overlay.setStyle('height', '0');
    };
};
