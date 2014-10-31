/*! http://mths.be/placeholder v2.0.7 by @mathias */
(function(q,f,d){function r(b){var a={},c=/^jQuery\d+$/;d.each(b.attributes,function(b,d){d.specified&&!c.test(d.name)&&(a[d.name]=d.value)});return a}function g(b,a){var c=d(this);if(this.value==c.attr("placeholder")&&c.hasClass("placeholder"))if(c.data("placeholder-password")){c=c.hide().next().show().attr("id",c.removeAttr("id").data("placeholder-id"));if(!0===b)return c[0].value=a;c.focus()}else this.value="",c.removeClass("placeholder"),this==m()&&this.select()}function k(){var b,a=d(this),c=
this.id;if(""==this.value){if("password"==this.type){if(!a.data("placeholder-textinput")){try{b=a.clone().attr({type:"text"})}catch(e){b=d("<input>").attr(d.extend(r(this),{type:"text"}))}b.removeAttr("name").data({"placeholder-password":a,"placeholder-id":c}).bind("focus.placeholder",g);a.data({"placeholder-textinput":b,"placeholder-id":c}).before(b)}a=a.removeAttr("id").hide().prev().attr("id",c).show()}a.addClass("placeholder");a[0].value=a.attr("placeholder")}else a.removeClass("placeholder")}
function m(){try{return f.activeElement}catch(b){}}var h="placeholder"in f.createElement("input"),l="placeholder"in f.createElement("textarea"),e=d.fn,n=d.valHooks,p=d.propHooks;h&&l?(e=e.placeholder=function(){return this},e.input=e.textarea=!0):(e=e.placeholder=function(){this.filter((h?"textarea":":input")+"[placeholder]").not(".placeholder").bind({"focus.placeholder":g,"blur.placeholder":k}).data("placeholder-enabled",!0).trigger("blur.placeholder");return this},e.input=h,e.textarea=l,e={get:function(b){var a=
d(b),c=a.data("placeholder-password");return c?c[0].value:a.data("placeholder-enabled")&&a.hasClass("placeholder")?"":b.value},set:function(b,a){var c=d(b),e=c.data("placeholder-password");if(e)return e[0].value=a;if(!c.data("placeholder-enabled"))return b.value=a;""==a?(b.value=a,b!=m()&&k.call(b)):c.hasClass("placeholder")?g.call(b,!0,a)||(b.value=a):b.value=a;return c}},h||(n.input=e,p.value=e),l||(n.textarea=e,p.value=e),d(function(){d(f).delegate("form","submit.placeholder",function(){var b=
d(".placeholder",this).each(g);setTimeout(function(){b.each(k)},10)})}),d(q).bind("beforeunload.placeholder",function(){d(".placeholder").each(function(){this.value=""})}))})(this,document,jQuery);

var Swiper=function(f,b){function h(a,b){return document.querySelectorAll?(b||document).querySelectorAll(a):jQuery(a,b)}function g(){var d=A-m;b.freeMode&&(d=A-m);b.slidesPerView>a.slides.length&&!b.centeredSlides&&(d=0);0>d&&(d=0);return d}function k(){function d(d){var c=new Image;c.onload=function(){"undefined"!==typeof a&&null!==a&&(void 0!==a.imagesLoaded&&a.imagesLoaded++,a.imagesLoaded===a.imagesToLoad.length&&(a.reInit(),b.onImagesReady&&a.fireCallback(b.onImagesReady,a)))};c.src=d}var c=
a.h.addEventListener,e="wrapper"===b.eventTarget?a.wrapper:a.container;a.browser.ie10||a.browser.ie11?(c(e,a.touchEvents.touchStart,B),c(document,a.touchEvents.touchMove,C),c(document,a.touchEvents.touchEnd,D)):(a.support.touch&&(c(e,"touchstart",B),c(e,"touchmove",C),c(e,"touchend",D)),b.simulateTouch&&(c(e,"mousedown",B),c(document,"mousemove",C),c(document,"mouseup",D)));b.autoResize&&c(window,"resize",a.resizeFix);u();a._wheelEvent=!1;if(b.mousewheelControl){void 0!==document.onmousewheel&&(a._wheelEvent=
"mousewheel");if(!a._wheelEvent)try{new WheelEvent("wheel"),a._wheelEvent="wheel"}catch(p){}a._wheelEvent||(a._wheelEvent="DOMMouseScroll");a._wheelEvent&&c(a.container,a._wheelEvent,I)}b.keyboardControl&&c(document,"keydown",E);if(b.updateOnImagesReady)for(a.imagesToLoad=h("img",a.container),c=0;c<a.imagesToLoad.length;c++)d(a.imagesToLoad[c].getAttribute("src"))}function u(){var d=a.h.addEventListener,c;if(b.preventLinks){var e=h("a",a.container);for(c=0;c<e.length;c++)d(e[c],"click",Q)}if(b.releaseFormElements)for(e=
h("input, textarea, select",a.container),c=0;c<e.length;c++)d(e[c],a.touchEvents.touchStart,R,!0);if(b.onSlideClick)for(c=0;c<a.slides.length;c++)d(a.slides[c],"click",S);if(b.onSlideTouch)for(c=0;c<a.slides.length;c++)d(a.slides[c],a.touchEvents.touchStart,T)}function v(){var d=a.h.removeEventListener,c;if(b.onSlideClick)for(c=0;c<a.slides.length;c++)d(a.slides[c],"click",S);if(b.onSlideTouch)for(c=0;c<a.slides.length;c++)d(a.slides[c],a.touchEvents.touchStart,T);if(b.releaseFormElements){var e=
h("input, textarea, select",a.container);for(c=0;c<e.length;c++)d(e[c],a.touchEvents.touchStart,R,!0)}if(b.preventLinks)for(e=h("a",a.container),c=0;c<e.length;c++)d(e[c],"click",Q)}function E(b){var c=b.keyCode||b.charCode;if(!(b.shiftKey||b.altKey||b.ctrlKey||b.metaKey)){if(37===c||39===c||38===c||40===c){for(var e=!1,p=a.h.getOffset(a.container),f=a.h.windowScroll().left,g=a.h.windowScroll().top,h=a.h.windowWidth(),k=a.h.windowHeight(),p=[[p.left,p.top],[p.left+a.width,p.top],[p.left,p.top+a.height],
[p.left+a.width,p.top+a.height]],m=0;m<p.length;m++){var l=p[m];l[0]>=f&&l[0]<=f+h&&l[1]>=g&&l[1]<=g+k&&(e=!0)}if(!e)return}if(n){if(37===c||39===c)b.preventDefault?b.preventDefault():b.returnValue=!1;39===c&&a.swipeNext();37===c&&a.swipePrev()}else{if(38===c||40===c)b.preventDefault?b.preventDefault():b.returnValue=!1;40===c&&a.swipeNext();38===c&&a.swipePrev()}}}function I(d){var c=a._wheelEvent,e=0;if(d.detail)e=-d.detail;else if("mousewheel"===c)if(b.mousewheelControlForceToAxis)if(n)if(Math.abs(d.wheelDeltaX)>
Math.abs(d.wheelDeltaY))e=d.wheelDeltaX;else return;else if(Math.abs(d.wheelDeltaY)>Math.abs(d.wheelDeltaX))e=d.wheelDeltaY;else return;else e=d.wheelDelta;else if("DOMMouseScroll"===c)e=-d.detail;else if("wheel"===c)if(b.mousewheelControlForceToAxis)if(n)if(Math.abs(d.deltaX)>Math.abs(d.deltaY))e=-d.deltaX;else return;else if(Math.abs(d.deltaY)>Math.abs(d.deltaX))e=-d.deltaY;else return;else e=Math.abs(d.deltaX)>Math.abs(d.deltaY)?-d.deltaX:-d.deltaY;if(b.freeMode){if(c=a.getWrapperTranslate()+e,
0<c&&(c=0),c<-g()&&(c=-g()),a.setWrapperTransition(0),a.setWrapperTranslate(c),a.updateActiveSlide(c),0===c||c===-g())return}else 60<(new Date).getTime()-U&&(0>e?a.swipeNext():a.swipePrev()),U=(new Date).getTime();b.autoplay&&a.stopAutoplay(!0);d.preventDefault?d.preventDefault():d.returnValue=!1;return!1}function S(d){a.allowSlideClick&&(V(d),a.fireCallback(b.onSlideClick,a,d))}function T(d){V(d);a.fireCallback(b.onSlideTouch,a,d)}function V(d){if(d.currentTarget)a.clickedSlide=d.currentTarget;else{d=
d.srcElement;do{if(-1<d.className.indexOf(b.slideClass))break;d=d.parentNode}while(d);a.clickedSlide=d}a.clickedSlideIndex=a.slides.indexOf(a.clickedSlide);a.clickedSlideLoopIndex=a.clickedSlideIndex-(a.loopedSlides||0)}function Q(d){if(!a.allowLinks)return d.preventDefault?d.preventDefault():d.returnValue=!1,b.preventLinksPropagation&&"stopPropagation"in d&&d.stopPropagation(),!1}function R(a){a.stopPropagation?a.stopPropagation():a.returnValue=!1;return!1}function B(d){b.preventLinks&&(a.allowLinks=
!0);if(a.isTouched||b.onlyExternal)return!1;var c=d.target||d.srcElement;document.activeElement&&document.activeElement!==c&&document.activeElement.blur();var e=["input","select","textarea"],p;if(p=b.noSwiping&&c){p=c;var f=!1;do-1<p.className.indexOf(b.noSwipingClass)&&(f=!0),p=p.parentElement;while(!f&&p.parentElement&&-1===p.className.indexOf(b.wrapperClass));!f&&-1<p.className.indexOf(b.wrapperClass)&&-1<p.className.indexOf(b.noSwipingClass)&&(f=!0);p=f}if(p)return!1;J=!1;a.isTouched=!0;w="touchstart"===
d.type;w&&1!==d.targetTouches.length||(a.callPlugins("onTouchStartBegin"),!w&&!a.isAndroid&&0>e.indexOf(c.tagName.toLowerCase())&&(d.preventDefault?d.preventDefault():d.returnValue=!1),c=w?d.targetTouches[0].pageX:d.pageX||d.clientX,e=w?d.targetTouches[0].pageY:d.pageY||d.clientY,a.touches.startX=a.touches.currentX=c,a.touches.startY=a.touches.currentY=e,a.touches.start=a.touches.current=n?c:e,a.setWrapperTransition(0),a.positions.start=a.positions.current=a.getWrapperTranslate(),a.setWrapperTranslate(a.positions.start),
a.times.start=(new Date).getTime(),y=void 0,0<b.moveStartThreshold&&(K=!1),b.onTouchStart&&a.fireCallback(b.onTouchStart,a,d),a.callPlugins("onTouchStartEnd"))}function C(d){if(a.isTouched&&!b.onlyExternal&&(!w||"mousemove"!==d.type)){var c=w?d.targetTouches[0].pageX:d.pageX||d.clientX,e=w?d.targetTouches[0].pageY:d.pageY||d.clientY;"undefined"===typeof y&&n&&(y=!!(y||Math.abs(e-a.touches.startY)>Math.abs(c-a.touches.startX)));"undefined"!==typeof y||n||(y=!!(y||Math.abs(e-a.touches.startY)<Math.abs(c-
a.touches.startX)));if(y)a.isTouched=!1;else{if(n){if(!b.swipeToNext&&c<a.touches.startX||!b.swipeToPrev&&c>a.touches.startX)return}else if(!b.swipeToNext&&e<a.touches.startY||!b.swipeToPrev&&e>a.touches.startY)return;if(d.assignedToSwiper)a.isTouched=!1;else if(d.assignedToSwiper=!0,b.preventLinks&&(a.allowLinks=!1),b.onSlideClick&&(a.allowSlideClick=!1),b.autoplay&&a.stopAutoplay(!0),!w||1===d.touches.length){a.isMoved||(a.callPlugins("onTouchMoveStart"),b.loop&&(a.fixLoop(),a.positions.start=a.getWrapperTranslate()),
b.onTouchMoveStart&&a.fireCallback(b.onTouchMoveStart,a));a.isMoved=!0;d.preventDefault?d.preventDefault():d.returnValue=!1;a.touches.current=n?c:e;a.positions.current=(a.touches.current-a.touches.start)*b.touchRatio+a.positions.start;0<a.positions.current&&b.onResistanceBefore&&a.fireCallback(b.onResistanceBefore,a,a.positions.current);a.positions.current<-g()&&b.onResistanceAfter&&a.fireCallback(b.onResistanceAfter,a,Math.abs(a.positions.current+g()));if(b.resistance&&"100%"!==b.resistance&&(0<
a.positions.current&&(c=1-a.positions.current/m/2,a.positions.current=.5>c?m/2:a.positions.current*c),a.positions.current<-g())){var e=(a.touches.current-a.touches.start)*b.touchRatio+(g()+a.positions.start),c=(m+e)/m,e=a.positions.current-e*(1-c)/2,p=-g()-m/2;a.positions.current=e<p||0>=c?p:e}b.resistance&&"100%"===b.resistance&&(0<a.positions.current&&(!b.freeMode||b.freeModeFluid)&&(a.positions.current=0),a.positions.current<-g()&&(!b.freeMode||b.freeModeFluid)&&(a.positions.current=-g()));if(b.followFinger){if(b.moveStartThreshold)if(Math.abs(a.touches.current-
a.touches.start)>b.moveStartThreshold||K){if(!K){K=!0;a.touches.start=a.touches.current;return}a.setWrapperTranslate(a.positions.current)}else a.positions.current=a.positions.start;else a.setWrapperTranslate(a.positions.current);(b.freeMode||b.watchActiveIndex)&&a.updateActiveSlide(a.positions.current);b.grabCursor&&(a.container.style.cursor="move",a.container.style.cursor="grabbing",a.container.style.cursor="-moz-grabbin",a.container.style.cursor="-webkit-grabbing");G||(G=a.touches.current);L||(L=
(new Date).getTime());a.velocity=(a.touches.current-G)/((new Date).getTime()-L)/2;2>Math.abs(a.touches.current-G)&&(a.velocity=0);G=a.touches.current;L=(new Date).getTime();a.callPlugins("onTouchMoveEnd");b.onTouchMove&&a.fireCallback(b.onTouchMove,a,d);return!1}}}}}function D(d){y&&a.swipeReset();if(!b.onlyExternal&&a.isTouched){a.isTouched=!1;b.grabCursor&&(a.container.style.cursor="move",a.container.style.cursor="grab",a.container.style.cursor="-moz-grab",a.container.style.cursor="-webkit-grab");
a.positions.current||0===a.positions.current||(a.positions.current=a.positions.start);b.followFinger&&a.setWrapperTranslate(a.positions.current);a.times.end=(new Date).getTime();a.touches.diff=a.touches.current-a.touches.start;a.touches.abs=Math.abs(a.touches.diff);a.positions.diff=a.positions.current-a.positions.start;a.positions.abs=Math.abs(a.positions.diff);var c=a.positions.diff,e=a.positions.abs,p=a.times.end-a.times.start;5>e&&300>p&&!1===a.allowLinks&&(b.freeMode||0===e||a.swipeReset(),b.preventLinks&&
(a.allowLinks=!0),b.onSlideClick&&(a.allowSlideClick=!0));setTimeout(function(){"undefined"!==typeof a&&null!==a&&(b.preventLinks&&(a.allowLinks=!0),b.onSlideClick&&(a.allowSlideClick=!0))},100);var f=g();if(!a.isMoved&&b.freeMode)a.isMoved=!1;else if(!a.isMoved||0<a.positions.current||a.positions.current<-f)a.swipeReset();else if(a.isMoved=!1,b.freeMode){if(b.freeModeFluid){var e=1E3*b.momentumRatio,c=a.positions.current+a.velocity*e,h=!1,x,k=20*Math.abs(a.velocity)*b.momentumBounceRatio;c<-f&&(b.momentumBounce&&
a.support.transitions?(c+f<-k&&(c=-f-k),x=-f,J=h=!0):c=-f);0<c&&(b.momentumBounce&&a.support.transitions?(c>k&&(c=k),x=0,J=h=!0):c=0);0!==a.velocity&&(e=Math.abs((c-a.positions.current)/a.velocity));a.setWrapperTranslate(c);a.setWrapperTransition(e);b.momentumBounce&&h&&a.wrapperTransitionEnd(function(){J&&(b.onMomentumBounce&&a.fireCallback(b.onMomentumBounce,a),a.callPlugins("onMomentumBounce"),a.setWrapperTranslate(x),a.setWrapperTransition(300))});a.updateActiveSlide(c)}(!b.freeModeFluid||300<=
p)&&a.updateActiveSlide(a.positions.current)}else{H=0>c?"toNext":"toPrev";"toNext"===H&&300>=p&&(30>e||!b.shortSwipes?a.swipeReset():a.swipeNext(!0));"toPrev"===H&&300>=p&&(30>e||!b.shortSwipes?a.swipeReset():a.swipePrev(!0));f=0;if("auto"===b.slidesPerView){for(var c=Math.abs(a.getWrapperTranslate()),l=h=0;l<a.slides.length;l++)if(k=n?a.slides[l].getWidth(!0,b.roundLengths):a.slides[l].getHeight(!0,b.roundLengths),h+=k,h>c){f=k;break}f>m&&(f=m)}else f=q*b.slidesPerView;"toNext"===H&&300<p&&(e>=f*
b.longSwipesRatio?a.swipeNext(!0):a.swipeReset());"toPrev"===H&&300<p&&(e>=f*b.longSwipesRatio?a.swipePrev(!0):a.swipeReset())}b.onTouchEnd&&a.fireCallback(b.onTouchEnd,a,d);a.callPlugins("onTouchEnd")}}function W(a,b){var e=document.createElement("div");e.innerHTML=b;e=e.firstChild;e.className+=" "+a;return e.outerHTML}function M(d,c,e){function f(){x+=k*(+new Date-g)/(1E3/60);(n="toNext"===m?x>d:x<d)?(a.setWrapperTranslate(Math.ceil(x)),a._DOMAnimating=!0,window.setTimeout(function(){f()},1E3/60)):
(b.onSlideChangeEnd&&("to"===c?!0===e.runCallbacks&&a.fireCallback(b.onSlideChangeEnd,a,m):a.fireCallback(b.onSlideChangeEnd,a,m)),a.setWrapperTranslate(d),a._DOMAnimating=!1)}var h="to"===c&&0<=e.speed?e.speed:b.speed,g=+new Date;if(a.support.transitions||!b.DOMAnimation)a.setWrapperTranslate(d),a.setWrapperTransition(h);else{var x=a.getWrapperTranslate(),k=Math.ceil((d-x)/h*(1E3/60)),m=x>d?"toNext":"toPrev",n="toNext"===m?x>d:x<d;if(a._DOMAnimating)return;f()}a.updateActiveSlide(d);b.onSlideNext&&
"next"===c&&a.fireCallback(b.onSlideNext,a,d);b.onSlidePrev&&"prev"===c&&a.fireCallback(b.onSlidePrev,a,d);b.onSlideReset&&"reset"===c&&a.fireCallback(b.onSlideReset,a,d);("next"===c||"prev"===c||"to"===c&&!0===e.runCallbacks)&&Z(c)}function Z(d){a.callPlugins("onSlideChangeStart");if(b.onSlideChangeStart)if(b.queueStartCallbacks&&a.support.transitions){if(a._queueStartCallbacks)return;a._queueStartCallbacks=!0;a.fireCallback(b.onSlideChangeStart,a,d);a.wrapperTransitionEnd(function(){a._queueStartCallbacks=
!1})}else a.fireCallback(b.onSlideChangeStart,a,d);b.onSlideChangeEnd&&(a.support.transitions?b.queueEndCallbacks?a._queueEndCallbacks||(a._queueEndCallbacks=!0,a.wrapperTransitionEnd(function(c){a.fireCallback(b.onSlideChangeEnd,c,d)})):a.wrapperTransitionEnd(function(c){a.fireCallback(b.onSlideChangeEnd,c,d)}):b.DOMAnimation||setTimeout(function(){a.fireCallback(b.onSlideChangeEnd,a,d)},10))}function X(){var b=a.paginationButtons;if(b)for(var c=0;c<b.length;c++)a.h.removeEventListener(b[c],"click",
Y)}function Y(d){var c;d=d.target||d.srcElement;for(var e=a.paginationButtons,f=0;f<e.length;f++)d===e[f]&&(c=f);b.autoplay&&a.stopAutoplay(!0);a.swipeTo(c)}function P(){s=setTimeout(function(){b.loop?(a.fixLoop(),a.swipeNext(!0)):a.swipeNext(!0)||(b.autoplayStopOnLast?(clearTimeout(s),s=void 0):a.swipeTo(0));a.wrapperTransitionEnd(function(){"undefined"!==typeof s&&P()})},b.autoplay)}if(!document.body.outerHTML&&document.body.__defineGetter__&&HTMLElement){var r=HTMLElement.prototype;r.__defineGetter__&&
r.__defineGetter__("outerHTML",function(){return(new XMLSerializer).serializeToString(this)})}window.getComputedStyle||(window.getComputedStyle=function(a,b){this.el=a;this.getPropertyValue=function(b){var c=/(\-([a-z]){1})/g;"float"===b&&(b="styleFloat");c.test(b)&&(b=b.replace(c,function(a,b,d){return d.toUpperCase()}));return a.currentStyle[b]?a.currentStyle[b]:null};return this});Array.prototype.indexOf||(Array.prototype.indexOf=function(a,b){for(var e=b||0,f=this.length;e<f;e++)if(this[e]===
a)return e;return-1});if((document.querySelectorAll||window.jQuery)&&"undefined"!==typeof f&&(f.nodeType||0!==h(f).length)){var a=this;a.touches={start:0,startX:0,startY:0,current:0,currentX:0,currentY:0,diff:0,abs:0};a.positions={start:0,abs:0,diff:0,current:0};a.times={start:0,end:0};a.id=(new Date).getTime();a.container=f.nodeType?f:h(f)[0];a.isTouched=!1;a.isMoved=!1;a.activeIndex=0;a.centerIndex=0;a.activeLoaderIndex=0;a.activeLoopIndex=0;a.previousIndex=null;a.velocity=0;a.snapGrid=[];a.slidesGrid=
[];a.imagesToLoad=[];a.imagesLoaded=0;a.wrapperLeft=0;a.wrapperRight=0;a.wrapperTop=0;a.wrapperBottom=0;a.isAndroid=0<=navigator.userAgent.toLowerCase().indexOf("android");var N,q,A,H,y,m,r={eventTarget:"wrapper",mode:"horizontal",touchRatio:1,speed:300,freeMode:!1,freeModeFluid:!1,momentumRatio:1,momentumBounce:!0,momentumBounceRatio:1,slidesPerView:1,slidesPerGroup:1,slidesPerViewFit:!0,simulateTouch:!0,followFinger:!0,shortSwipes:!0,longSwipesRatio:.5,moveStartThreshold:!1,onlyExternal:!1,createPagination:!0,
pagination:!1,paginationElement:"span",paginationClickable:!1,paginationAsRange:!0,resistance:!0,scrollContainer:!1,preventLinks:!0,preventLinksPropagation:!1,noSwiping:!1,noSwipingClass:"swiper-no-swiping",initialSlide:0,keyboardControl:!1,mousewheelControl:!1,mousewheelControlForceToAxis:!1,useCSS3Transforms:!0,autoplay:!1,autoplayDisableOnInteraction:!0,autoplayStopOnLast:!1,loop:!1,loopAdditionalSlides:0,roundLengths:!1,calculateHeight:!1,cssWidthAndHeight:!1,updateOnImagesReady:!0,releaseFormElements:!0,
watchActiveIndex:!1,visibilityFullFit:!1,offsetPxBefore:0,offsetPxAfter:0,offsetSlidesBefore:0,offsetSlidesAfter:0,centeredSlides:!1,queueStartCallbacks:!1,queueEndCallbacks:!1,autoResize:!0,resizeReInit:!1,DOMAnimation:!0,loader:{slides:[],slidesHTMLType:"inner",surroundGroups:1,logic:"reload",loadAllSlides:!1},swipeToPrev:!0,swipeToNext:!0,slideElement:"div",slideClass:"swiper-slide",slideActiveClass:"swiper-slide-active",slideVisibleClass:"swiper-slide-visible",slideDuplicateClass:"swiper-slide-duplicate",
wrapperClass:"swiper-wrapper",paginationElementClass:"swiper-pagination-switch",paginationActiveClass:"swiper-active-switch",paginationVisibleClass:"swiper-visible-switch"};b=b||{};for(var l in r)if(l in b&&"object"===typeof b[l])for(var F in r[l])F in b[l]||(b[l][F]=r[l][F]);else l in b||(b[l]=r[l]);a.params=b;b.scrollContainer&&(b.freeMode=!0,b.freeModeFluid=!0);b.loop&&(b.resistance="100%");var n="horizontal"===b.mode;l=["mousedown","mousemove","mouseup"];a.browser.ie10&&(l=["MSPointerDown","MSPointerMove",
"MSPointerUp"]);a.browser.ie11&&(l=["pointerdown","pointermove","pointerup"]);a.touchEvents={touchStart:a.support.touch||!b.simulateTouch?"touchstart":l[0],touchMove:a.support.touch||!b.simulateTouch?"touchmove":l[1],touchEnd:a.support.touch||!b.simulateTouch?"touchend":l[2]};for(l=a.container.childNodes.length-1;0<=l;l--)if(a.container.childNodes[l].className)for(F=a.container.childNodes[l].className.split(/\s+/),r=0;r<F.length;r++)F[r]===b.wrapperClass&&(N=a.container.childNodes[l]);a.wrapper=N;
a._extendSwiperSlide=function(d){d.append=function(){b.loop?d.insertAfter(a.slides.length-a.loopedSlides):(a.wrapper.appendChild(d),a.reInit());return d};d.prepend=function(){b.loop?(a.wrapper.insertBefore(d,a.slides[a.loopedSlides]),a.removeLoopedSlides(),a.calcSlides(),a.createLoop()):a.wrapper.insertBefore(d,a.wrapper.firstChild);a.reInit();return d};d.insertAfter=function(c){if("undefined"===typeof c)return!1;b.loop?((c=a.slides[c+1+a.loopedSlides])?a.wrapper.insertBefore(d,c):a.wrapper.appendChild(d),
a.removeLoopedSlides(),a.calcSlides(),a.createLoop()):(c=a.slides[c+1],a.wrapper.insertBefore(d,c));a.reInit();return d};d.clone=function(){return a._extendSwiperSlide(d.cloneNode(!0))};d.remove=function(){a.wrapper.removeChild(d);a.reInit()};d.html=function(a){if("undefined"===typeof a)return d.innerHTML;d.innerHTML=a;return d};d.index=function(){for(var b,e=a.slides.length-1;0<=e;e--)d===a.slides[e]&&(b=e);return b};d.isActive=function(){return d.index()===a.activeIndex?!0:!1};d.swiperSlideDataStorage||
(d.swiperSlideDataStorage={});d.getData=function(a){return d.swiperSlideDataStorage[a]};d.setData=function(a,b){d.swiperSlideDataStorage[a]=b;return d};d.data=function(a,b){if("undefined"===typeof b)return d.getAttribute("data-"+a);d.setAttribute("data-"+a,b);return d};d.getWidth=function(b,e){return a.h.getWidth(d,b,e)};d.getHeight=function(b,e){return a.h.getHeight(d,b,e)};d.getOffset=function(){return a.h.getOffset(d)};return d};a.calcSlides=function(d){var c=a.slides?a.slides.length:!1;a.slides=
[];a.displaySlides=[];for(var e=0;e<a.wrapper.childNodes.length;e++)if(a.wrapper.childNodes[e].className)for(var f=a.wrapper.childNodes[e].className.split(/\s+/),h=0;h<f.length;h++)f[h]===b.slideClass&&a.slides.push(a.wrapper.childNodes[e]);for(e=a.slides.length-1;0<=e;e--)a._extendSwiperSlide(a.slides[e]);!1===c||c===a.slides.length&&!d||(v(),u(),a.updateActiveSlide(),a.params.pagination&&a.createPagination(),a.callPlugins("numberOfSlidesChanged"))};a.createSlide=function(d,c,e){c=c||a.params.slideClass;
e=e||b.slideElement;e=document.createElement(e);e.innerHTML=d||"";e.className=c;return a._extendSwiperSlide(e)};a.appendSlide=function(b,c,e){if(b)return b.nodeType?a._extendSwiperSlide(b).append():a.createSlide(b,c,e).append()};a.prependSlide=function(b,c,e){if(b)return b.nodeType?a._extendSwiperSlide(b).prepend():a.createSlide(b,c,e).prepend()};a.insertSlideAfter=function(b,c,e,f){return"undefined"===typeof b?!1:c.nodeType?a._extendSwiperSlide(c).insertAfter(b):a.createSlide(c,e,f).insertAfter(b)};
a.removeSlide=function(d){if(a.slides[d]){if(b.loop){if(!a.slides[d+a.loopedSlides])return!1;a.slides[d+a.loopedSlides].remove();a.removeLoopedSlides();a.calcSlides();a.createLoop()}else a.slides[d].remove();return!0}return!1};a.removeLastSlide=function(){return 0<a.slides.length?(b.loop?(a.slides[a.slides.length-1-a.loopedSlides].remove(),a.removeLoopedSlides(),a.calcSlides(),a.createLoop()):a.slides[a.slides.length-1].remove(),!0):!1};a.removeAllSlides=function(){for(var b=a.slides.length-1;0<=
b;b--)a.slides[b].remove()};a.getSlide=function(b){return a.slides[b]};a.getLastSlide=function(){return a.slides[a.slides.length-1]};a.getFirstSlide=function(){return a.slides[0]};a.activeSlide=function(){return a.slides[a.activeIndex]};a.fireCallback=function(d,c,e,f,h,g){if("[object Array]"===Object.prototype.toString.call(d))for(var k=0;k<d.length;k++){if("function"===typeof d[k])d[k](c,e,f,h,g)}else"[object String]"===Object.prototype.toString.call(d)?b["on"+d]&&a.fireCallback(b["on"+d],c,e,f,
h,g):d(c,e,f,h,g)};a.addCallback=function(a,b){var e;if(this.params["on"+a]){e="[object Array]"===Object.prototype.toString.apply(this.params["on"+a])?!0:!1;if(e)return this.params["on"+a].push(b);if("function"===typeof this.params["on"+a])return e=this.params["on"+a],this.params["on"+a]=[],this.params["on"+a].push(e),this.params["on"+a].push(b)}else return this.params["on"+a]=[],this.params["on"+a].push(b)};a.removeCallbacks=function(b){a.params["on"+b]&&(a.params["on"+b]=null)};var O=[],z;for(z in a.plugins)b[z]&&
(l=a.plugins[z](a,b[z]))&&O.push(l);a.callPlugins=function(a,b){b||(b={});for(var e=0;e<O.length;e++)if(a in O[e])O[e][a](b)};!a.browser.ie10&&!a.browser.ie11||b.onlyExternal||a.wrapper.classList.add("swiper-wp8-"+(n?"horizontal":"vertical"));b.freeMode&&(a.container.className+=" swiper-free-mode");a.initialized=!1;a.init=function(d,c){var e=a.h.getWidth(a.container,!1,b.roundLengths),f=a.h.getHeight(a.container,!1,b.roundLengths);if(e!==a.width||f!==a.height||d){a.width=e;a.height=f;var h,g,k;m=
n?e:f;var l=a.wrapper;d&&a.calcSlides(c);if("auto"===b.slidesPerView){var s=0,u=0;0<b.slidesOffset&&(l.style.paddingLeft="",l.style.paddingRight="",l.style.paddingTop="",l.style.paddingBottom="");l.style.width="";l.style.height="";0<b.offsetPxBefore&&(n?a.wrapperLeft=b.offsetPxBefore:a.wrapperTop=b.offsetPxBefore);0<b.offsetPxAfter&&(n?a.wrapperRight=b.offsetPxAfter:a.wrapperBottom=b.offsetPxAfter);b.centeredSlides&&(n?(a.wrapperLeft=(m-this.slides[0].getWidth(!0,b.roundLengths))/2,a.wrapperRight=
(m-a.slides[a.slides.length-1].getWidth(!0,b.roundLengths))/2):(a.wrapperTop=(m-a.slides[0].getHeight(!0,b.roundLengths))/2,a.wrapperBottom=(m-a.slides[a.slides.length-1].getHeight(!0,b.roundLengths))/2));n?(0<=a.wrapperLeft&&(l.style.paddingLeft=a.wrapperLeft+"px"),0<=a.wrapperRight&&(l.style.paddingRight=a.wrapperRight+"px")):(0<=a.wrapperTop&&(l.style.paddingTop=a.wrapperTop+"px"),0<=a.wrapperBottom&&(l.style.paddingBottom=a.wrapperBottom+"px"));var v=g=0;a.snapGrid=[];a.slidesGrid=[];for(k=h=
0;k<a.slides.length;k++){e=a.slides[k].getWidth(!0,b.roundLengths);f=a.slides[k].getHeight(!0,b.roundLengths);b.calculateHeight&&(h=Math.max(h,f));var r=n?e:f;if(b.centeredSlides){var t=k===a.slides.length-1?0:a.slides[k+1].getWidth(!0,b.roundLengths),w=k===a.slides.length-1?0:a.slides[k+1].getHeight(!0,b.roundLengths),t=n?t:w;if(r>m){if(b.slidesPerViewFit)a.snapGrid.push(g+a.wrapperLeft),a.snapGrid.push(g+r-m+a.wrapperLeft);else for(w=0;w<=Math.floor(r/(m+a.wrapperLeft));w++)0===w?a.snapGrid.push(g+
a.wrapperLeft):a.snapGrid.push(g+a.wrapperLeft+m*w);a.slidesGrid.push(g+a.wrapperLeft)}else a.snapGrid.push(v),a.slidesGrid.push(v);v+=r/2+t/2}else{if(r>m)if(b.slidesPerViewFit)a.snapGrid.push(g),a.snapGrid.push(g+r-m);else if(0!==m)for(t=0;t<=Math.floor(r/m);t++)a.snapGrid.push(g+m*t);else a.snapGrid.push(g);else a.snapGrid.push(g);a.slidesGrid.push(g)}g+=r;s+=e;u+=f}b.calculateHeight&&(a.height=h);n?(A=s+a.wrapperRight+a.wrapperLeft,l.style.width=s+"px",l.style.height=a.height+"px"):(A=u+a.wrapperTop+
a.wrapperBottom,l.style.width=a.width+"px",l.style.height=u+"px")}else if(b.scrollContainer)l.style.width="",l.style.height="",h=a.slides[0].getWidth(!0,b.roundLengths),g=a.slides[0].getHeight(!0,b.roundLengths),A=n?h:g,l.style.width=h+"px",l.style.height=g+"px",q=n?h:g;else{if(b.calculateHeight){g=h=0;n||(a.container.style.height="");l.style.height="";for(k=0;k<a.slides.length;k++)a.slides[k].style.height="",h=Math.max(a.slides[k].getHeight(!0),h),n||(g+=a.slides[k].getHeight(!0));f=h;a.height=f;
n?g=f:(m=f,a.container.style.height=m+"px")}else f=n?a.height:a.height/b.slidesPerView,b.roundLengths&&(f=Math.ceil(f)),g=n?a.height:a.slides.length*f;e=n?a.width/b.slidesPerView:a.width;b.roundLengths&&(e=Math.ceil(e));h=n?a.slides.length*e:a.width;q=n?e:f;0<b.offsetSlidesBefore&&(n?a.wrapperLeft=q*b.offsetSlidesBefore:a.wrapperTop=q*b.offsetSlidesBefore);0<b.offsetSlidesAfter&&(n?a.wrapperRight=q*b.offsetSlidesAfter:a.wrapperBottom=q*b.offsetSlidesAfter);0<b.offsetPxBefore&&(n?a.wrapperLeft=b.offsetPxBefore:
a.wrapperTop=b.offsetPxBefore);0<b.offsetPxAfter&&(n?a.wrapperRight=b.offsetPxAfter:a.wrapperBottom=b.offsetPxAfter);b.centeredSlides&&(n?(a.wrapperLeft=(m-q)/2,a.wrapperRight=(m-q)/2):(a.wrapperTop=(m-q)/2,a.wrapperBottom=(m-q)/2));n?(0<a.wrapperLeft&&(l.style.paddingLeft=a.wrapperLeft+"px"),0<a.wrapperRight&&(l.style.paddingRight=a.wrapperRight+"px")):(0<a.wrapperTop&&(l.style.paddingTop=a.wrapperTop+"px"),0<a.wrapperBottom&&(l.style.paddingBottom=a.wrapperBottom+"px"));A=n?h+a.wrapperRight+a.wrapperLeft:
g+a.wrapperTop+a.wrapperBottom;0<parseFloat(h)&&(!b.cssWidthAndHeight||"height"===b.cssWidthAndHeight)&&(l.style.width=h+"px");0<parseFloat(g)&&(!b.cssWidthAndHeight||"width"===b.cssWidthAndHeight)&&(l.style.height=g+"px");g=0;a.snapGrid=[];a.slidesGrid=[];for(k=0;k<a.slides.length;k++)a.snapGrid.push(g),a.slidesGrid.push(g),g+=q,0<parseFloat(e)&&(!b.cssWidthAndHeight||"height"===b.cssWidthAndHeight)&&(a.slides[k].style.width=e+"px"),0<parseFloat(f)&&(!b.cssWidthAndHeight||"width"===b.cssWidthAndHeight)&&
(a.slides[k].style.height=f+"px")}a.initialized?(a.callPlugins("onInit"),b.onInit&&a.fireCallback(b.onInit,a)):(a.callPlugins("onFirstInit"),b.onFirstInit&&a.fireCallback(b.onFirstInit,a));a.initialized=!0}};a.reInit=function(b){a.init(!0,b)};a.resizeFix=function(d){a.callPlugins("beforeResizeFix");a.init(b.resizeReInit||d);b.freeMode?a.getWrapperTranslate()<-g()&&(a.setWrapperTransition(0),a.setWrapperTranslate(-g())):(a.swipeTo(b.loop?a.activeLoopIndex:a.activeIndex,0,!1),b.autoplay&&(a.support.transitions&&
"undefined"!==typeof s?"undefined"!==typeof s&&(clearTimeout(s),s=void 0,a.startAutoplay()):"undefined"!==typeof t&&(clearInterval(t),t=void 0,a.startAutoplay())));a.callPlugins("afterResizeFix")};a.destroy=function(){var d=a.h.removeEventListener,c="wrapper"===b.eventTarget?a.wrapper:a.container;a.browser.ie10||a.browser.ie11?(d(c,a.touchEvents.touchStart,B),d(document,a.touchEvents.touchMove,C),d(document,a.touchEvents.touchEnd,D)):(a.support.touch&&(d(c,"touchstart",B),d(c,"touchmove",C),d(c,"touchend",
D)),b.simulateTouch&&(d(c,"mousedown",B),d(document,"mousemove",C),d(document,"mouseup",D)));b.autoResize&&d(window,"resize",a.resizeFix);v();b.paginationClickable&&X();b.mousewheelControl&&a._wheelEvent&&d(a.container,a._wheelEvent,I);b.keyboardControl&&d(document,"keydown",E);b.autoplay&&a.stopAutoplay();a.callPlugins("onDestroy");a=null};a.disableKeyboardControl=function(){b.keyboardControl=!1;a.h.removeEventListener(document,"keydown",E)};a.enableKeyboardControl=function(){b.keyboardControl=!0;
a.h.addEventListener(document,"keydown",E)};var U=(new Date).getTime();a.disableMousewheelControl=function(){if(!a._wheelEvent)return!1;b.mousewheelControl=!1;a.h.removeEventListener(a.container,a._wheelEvent,I);return!0};a.enableMousewheelControl=function(){if(!a._wheelEvent)return!1;b.mousewheelControl=!0;a.h.addEventListener(a.container,a._wheelEvent,I);return!0};b.grabCursor&&(z=a.container.style,z.cursor="move",z.cursor="grab",z.cursor="-moz-grab",z.cursor="-webkit-grab");a.allowSlideClick=!0;
a.allowLinks=!0;var w=!1,K,J=!0,G,L;a.swipeNext=function(d){!d&&b.loop&&a.fixLoop();!d&&b.autoplay&&a.stopAutoplay(!0);a.callPlugins("onSwipeNext");var c=d=a.getWrapperTranslate();if("auto"===b.slidesPerView)for(var e=0;e<a.snapGrid.length;e++){if(-d>=a.snapGrid[e]&&-d<a.snapGrid[e+1]){c=-a.snapGrid[e+1];break}}else c=q*b.slidesPerGroup,c=-(Math.floor(Math.abs(d)/Math.floor(c))*c+c);c<-g()&&(c=-g());if(c===d)return!1;M(c,"next");return!0};a.swipePrev=function(d){!d&&b.loop&&a.fixLoop();!d&&b.autoplay&&
a.stopAutoplay(!0);a.callPlugins("onSwipePrev");d=Math.ceil(a.getWrapperTranslate());var c;if("auto"===b.slidesPerView){c=0;for(var e=1;e<a.snapGrid.length;e++){if(-d===a.snapGrid[e]){c=-a.snapGrid[e-1];break}if(-d>a.snapGrid[e]&&-d<a.snapGrid[e+1]){c=-a.snapGrid[e];break}}}else c=q*b.slidesPerGroup,c*=-(Math.ceil(-d/c)-1);0<c&&(c=0);if(c===d)return!1;M(c,"prev");return!0};a.swipeReset=function(){a.callPlugins("onSwipeReset");var d=a.getWrapperTranslate(),c=q*b.slidesPerGroup;g();if("auto"===b.slidesPerView){for(var e=
c=0;e<a.snapGrid.length;e++){if(-d===a.snapGrid[e])return;if(-d>=a.snapGrid[e]&&-d<a.snapGrid[e+1]){c=0<a.positions.diff?-a.snapGrid[e+1]:-a.snapGrid[e];break}}-d>=a.snapGrid[a.snapGrid.length-1]&&(c=-a.snapGrid[a.snapGrid.length-1])}else c=0>d?Math.round(d/c)*c:0;d<=-g()&&(c=-g());b.scrollContainer&&(c=0>d?d:0);c<-g()&&(c=-g());b.scrollContainer&&m>q&&(c=0);if(c===d)return!1;M(c,"reset");return!0};a.swipeTo=function(d,c,e){d=parseInt(d,10);a.callPlugins("onSwipeTo",{index:d,speed:c});b.loop&&(d+=
a.loopedSlides);var f=a.getWrapperTranslate();if(!(d>a.slides.length-1||0>d)){var h;h="auto"===b.slidesPerView?-a.slidesGrid[d]:-d*q;h<-g()&&(h=-g());if(h===f)return!1;M(h,"to",{index:d,speed:c,runCallbacks:!1===e?!1:!0});return!0}};a._queueStartCallbacks=!1;a._queueEndCallbacks=!1;a.updateActiveSlide=function(d){if(a.initialized&&0!==a.slides.length){a.previousIndex=a.activeIndex;"undefined"===typeof d&&(d=a.getWrapperTranslate());0<d&&(d=0);var c;if("auto"===b.slidesPerView){if(a.activeIndex=a.slidesGrid.indexOf(-d),
0>a.activeIndex){for(c=0;c<a.slidesGrid.length-1&&!(-d>a.slidesGrid[c]&&-d<a.slidesGrid[c+1]);c++);var e=Math.abs(a.slidesGrid[c]+d),f=Math.abs(a.slidesGrid[c+1]+d);a.activeIndex=e<=f?c:c+1}}else a.activeIndex=Math[b.visibilityFullFit?"ceil":"round"](-d/q);a.activeIndex===a.slides.length&&(a.activeIndex=a.slides.length-1);0>a.activeIndex&&(a.activeIndex=0);if(a.slides[a.activeIndex]){a.calcVisibleSlides(d);if(a.support.classList){for(c=0;c<a.slides.length;c++)e=a.slides[c],e.classList.remove(b.slideActiveClass),
0<=a.visibleSlides.indexOf(e)?e.classList.add(b.slideVisibleClass):e.classList.remove(b.slideVisibleClass);a.slides[a.activeIndex].classList.add(b.slideActiveClass)}else{e=new RegExp("\\s*"+b.slideActiveClass);f=new RegExp("\\s*"+b.slideVisibleClass);for(c=0;c<a.slides.length;c++)a.slides[c].className=a.slides[c].className.replace(e,"").replace(f,""),0<=a.visibleSlides.indexOf(a.slides[c])&&(a.slides[c].className+=" "+b.slideVisibleClass);a.slides[a.activeIndex].className+=" "+b.slideActiveClass}b.loop?
(c=a.loopedSlides,a.activeLoopIndex=a.activeIndex-c,a.activeLoopIndex>=a.slides.length-2*c&&(a.activeLoopIndex=a.slides.length-2*c-a.activeLoopIndex),0>a.activeLoopIndex&&(a.activeLoopIndex=a.slides.length-2*c+a.activeLoopIndex),0>a.activeLoopIndex&&(a.activeLoopIndex=0)):a.activeLoopIndex=a.activeIndex;b.pagination&&a.updatePagination(d)}}};a.createPagination=function(d){b.paginationClickable&&a.paginationButtons&&X();a.paginationContainer=b.pagination.nodeType?b.pagination:h(b.pagination)[0];if(b.createPagination){var c=
"",e=a.slides.length;b.loop&&(e-=2*a.loopedSlides);for(var f=0;f<e;f++)c+="<"+b.paginationElement+' class="'+b.paginationElementClass+'"></'+b.paginationElement+">";a.paginationContainer.innerHTML=c}a.paginationButtons=h("."+b.paginationElementClass,a.paginationContainer);d||a.updatePagination();a.callPlugins("onCreatePagination");if(b.paginationClickable&&(d=a.paginationButtons))for(c=0;c<d.length;c++)a.h.addEventListener(d[c],"click",Y)};a.updatePagination=function(d){if(b.pagination&&!(1>a.slides.length)&&
h("."+b.paginationActiveClass,a.paginationContainer)){var c=a.paginationButtons;if(0!==c.length){for(var e=0;e<c.length;e++)c[e].className=b.paginationElementClass;e=b.loop?a.loopedSlides:0;if(b.paginationAsRange){a.visibleSlides||a.calcVisibleSlides(d);d=[];var f;for(f=0;f<a.visibleSlides.length;f++){var g=a.slides.indexOf(a.visibleSlides[f])-e;b.loop&&0>g&&(g=a.slides.length-2*a.loopedSlides+g);b.loop&&g>=a.slides.length-2*a.loopedSlides&&(g=a.slides.length-2*a.loopedSlides-g,g=Math.abs(g));d.push(g)}for(f=
0;f<d.length;f++)c[d[f]]&&(c[d[f]].className+=" "+b.paginationVisibleClass);b.loop?void 0!==c[a.activeLoopIndex]&&(c[a.activeLoopIndex].className+=" "+b.paginationActiveClass):c[a.activeIndex].className+=" "+b.paginationActiveClass}else b.loop?c[a.activeLoopIndex]&&(c[a.activeLoopIndex].className+=" "+b.paginationActiveClass+" "+b.paginationVisibleClass):c[a.activeIndex].className+=" "+b.paginationActiveClass+" "+b.paginationVisibleClass}}};a.calcVisibleSlides=function(d){var c=[],e=0,f=0,g=0;n&&
0<a.wrapperLeft&&(d+=a.wrapperLeft);!n&&0<a.wrapperTop&&(d+=a.wrapperTop);for(var h=0;h<a.slides.length;h++){var e=e+f,f="auto"===b.slidesPerView?n?a.h.getWidth(a.slides[h],!0,b.roundLengths):a.h.getHeight(a.slides[h],!0,b.roundLengths):q,g=e+f,k=!1;b.visibilityFullFit?(e>=-d&&g<=-d+m&&(k=!0),e<=-d&&g>=-d+m&&(k=!0)):(g>-d&&g<=-d+m&&(k=!0),e>=-d&&e<-d+m&&(k=!0),e<-d&&g>-d+m&&(k=!0));k&&c.push(a.slides[h])}0===c.length&&(c=[a.slides[a.activeIndex]]);a.visibleSlides=c};var s,t;a.startAutoplay=function(){if(a.support.transitions){if("undefined"!==
typeof s)return!1;b.autoplay&&(a.callPlugins("onAutoplayStart"),b.onAutoplayStart&&a.fireCallback(b.onAutoplayStart,a),P())}else{if("undefined"!==typeof t)return!1;b.autoplay&&(a.callPlugins("onAutoplayStart"),b.onAutoplayStart&&a.fireCallback(b.onAutoplayStart,a),t=setInterval(function(){b.loop?(a.fixLoop(),a.swipeNext(!0)):a.swipeNext(!0)||(b.autoplayStopOnLast?(clearInterval(t),t=void 0):a.swipeTo(0))},b.autoplay))}};a.stopAutoplay=function(d){a.support.transitions?s&&(s&&clearTimeout(s),s=void 0,
d&&!b.autoplayDisableOnInteraction&&a.wrapperTransitionEnd(function(){P()}),a.callPlugins("onAutoplayStop"),b.onAutoplayStop&&a.fireCallback(b.onAutoplayStop,a)):(t&&clearInterval(t),t=void 0,a.callPlugins("onAutoplayStop"),b.onAutoplayStop&&a.fireCallback(b.onAutoplayStop,a))};a.loopCreated=!1;a.removeLoopedSlides=function(){if(a.loopCreated)for(var b=0;b<a.slides.length;b++)!0===a.slides[b].getData("looped")&&a.wrapper.removeChild(a.slides[b])};a.createLoop=function(){if(0!==a.slides.length){a.loopedSlides=
"auto"===b.slidesPerView?b.loopedSlides||1:b.slidesPerView+b.loopAdditionalSlides;a.loopedSlides>a.slides.length&&(a.loopedSlides=a.slides.length);var d="",c="",e,f="",g=a.slides.length,h=Math.floor(a.loopedSlides/g),k=a.loopedSlides%g;for(e=0;e<h*g;e++){var l=e;e>=g&&(l=e-g*Math.floor(e/g));f+=a.slides[l].outerHTML}for(e=0;e<k;e++)c+=W(b.slideDuplicateClass,a.slides[e].outerHTML);for(e=g-k;e<g;e++)d+=W(b.slideDuplicateClass,a.slides[e].outerHTML);N.innerHTML=d+f+N.innerHTML+f+c;a.loopCreated=!0;
a.calcSlides();for(e=0;e<a.slides.length;e++)(e<a.loopedSlides||e>=a.slides.length-a.loopedSlides)&&a.slides[e].setData("looped",!0);a.callPlugins("onCreateLoop")}};a.fixLoop=function(){var d;if(a.activeIndex<a.loopedSlides)d=a.slides.length-3*a.loopedSlides+a.activeIndex,a.swipeTo(d,0,!1);else if("auto"===b.slidesPerView&&a.activeIndex>=2*a.loopedSlides||a.activeIndex>a.slides.length-2*b.slidesPerView)d=-a.slides.length+a.activeIndex+a.loopedSlides,a.swipeTo(d,0,!1)};a.loadSlides=function(){var d=
"";a.activeLoaderIndex=0;for(var c=b.loader.slides,e=b.loader.loadAllSlides?c.length:b.slidesPerView*(1+b.loader.surroundGroups),f=0;f<e;f++)d="outer"===b.loader.slidesHTMLType?d+c[f]:d+("<"+b.slideElement+' class="'+b.slideClass+'" data-swiperindex="'+f+'">'+c[f]+"</"+b.slideElement+">");a.wrapper.innerHTML=d;a.calcSlides(!0);b.loader.loadAllSlides||a.wrapperTransitionEnd(a.reloadSlides,!0)};a.reloadSlides=function(){var d=b.loader.slides,c=parseInt(a.activeSlide().data("swiperindex"),10);if(!(0>
c||c>d.length-1)){a.activeLoaderIndex=c;var e=Math.max(0,c-b.slidesPerView*b.loader.surroundGroups),f=Math.min(c+b.slidesPerView*(1+b.loader.surroundGroups)-1,d.length-1);0<c&&(a.setWrapperTranslate(-q*(c-e)),a.setWrapperTransition(0));if("reload"===b.loader.logic){for(var g=a.wrapper.innerHTML="",c=e;c<=f;c++)g+="outer"===b.loader.slidesHTMLType?d[c]:"<"+b.slideElement+' class="'+b.slideClass+'" data-swiperindex="'+c+'">'+d[c]+"</"+b.slideElement+">";a.wrapper.innerHTML=g}else{for(var g=1E3,h=0,
c=0;c<a.slides.length;c++){var k=a.slides[c].data("swiperindex");k<e||k>f?a.wrapper.removeChild(a.slides[c]):(g=Math.min(k,g),h=Math.max(k,h))}for(c=e;c<=f;c++)c<g&&(e=document.createElement(b.slideElement),e.className=b.slideClass,e.setAttribute("data-swiperindex",c),e.innerHTML=d[c],a.wrapper.insertBefore(e,a.wrapper.firstChild)),c>h&&(e=document.createElement(b.slideElement),e.className=b.slideClass,e.setAttribute("data-swiperindex",c),e.innerHTML=d[c],a.wrapper.appendChild(e))}a.reInit(!0)}};
a.calcSlides();0<b.loader.slides.length&&0===a.slides.length&&a.loadSlides();b.loop&&a.createLoop();a.init();k();b.pagination&&a.createPagination(!0);b.loop||0<b.initialSlide?a.swipeTo(b.initialSlide,0,!1):a.updateActiveSlide(0);b.autoplay&&a.startAutoplay();a.centerIndex=a.activeIndex;b.onSwiperCreated&&a.fireCallback(b.onSwiperCreated,a);a.callPlugins("onSwiperCreated")}};
Swiper.prototype={plugins:{},wrapperTransitionEnd:function(f,b){function h(E){if(E.target===k&&(f(g),g.params.queueEndCallbacks&&(g._queueEndCallbacks=!1),!b))for(v=0;v<u.length;v++)g.h.removeEventListener(k,u[v],h)}var g=this,k=g.wrapper,u=["webkitTransitionEnd","transitionend","oTransitionEnd","MSTransitionEnd","msTransitionEnd"],v;if(f)for(v=0;v<u.length;v++)g.h.addEventListener(k,u[v],h)},getWrapperTranslate:function(f){var b=this.wrapper,h,g;"undefined"===typeof f&&(f="horizontal"===this.params.mode?
"x":"y");this.support.transforms&&this.params.useCSS3Transforms?(b=window.getComputedStyle(b,null),window.WebKitCSSMatrix?b=new WebKitCSSMatrix("none"===b.webkitTransform?"":b.webkitTransform):(b=b.MozTransform||b.OTransform||b.MsTransform||b.msTransform||b.transform||b.getPropertyValue("transform").replace("translate(","matrix(1, 0, 0, 1,"),h=b.toString().split(",")),"x"===f&&(g=window.WebKitCSSMatrix?b.m41:16===h.length?parseFloat(h[12]):parseFloat(h[4])),"y"===f&&(g=window.WebKitCSSMatrix?b.m42:
16===h.length?parseFloat(h[13]):parseFloat(h[5]))):("x"===f&&(g=parseFloat(b.style.left,10)||0),"y"===f&&(g=parseFloat(b.style.top,10)||0));return g||0},setWrapperTranslate:function(f,b,h){var g=this.wrapper.style,k={x:0,y:0,z:0},u;3===arguments.length?(k.x=f,k.y=b,k.z=h):("undefined"===typeof b&&(b="horizontal"===this.params.mode?"x":"y"),k[b]=f);this.support.transforms&&this.params.useCSS3Transforms?(u=this.support.transforms3d?"translate3d("+k.x+"px, "+k.y+"px, "+k.z+"px)":"translate("+k.x+"px, "+
k.y+"px)",g.webkitTransform=g.MsTransform=g.msTransform=g.MozTransform=g.OTransform=g.transform=u):(g.left=k.x+"px",g.top=k.y+"px");this.callPlugins("onSetWrapperTransform",k);this.params.onSetWrapperTransform&&this.fireCallback(this.params.onSetWrapperTransform,this,k)},setWrapperTransition:function(f){var b=this.wrapper.style;b.webkitTransitionDuration=b.MsTransitionDuration=b.msTransitionDuration=b.MozTransitionDuration=b.OTransitionDuration=b.transitionDuration=f/1E3+"s";this.callPlugins("onSetWrapperTransition",
{duration:f});this.params.onSetWrapperTransition&&this.fireCallback(this.params.onSetWrapperTransition,this,f)},h:{getWidth:function(f,b,h){var g=window.getComputedStyle(f,null).getPropertyValue("width"),k=parseFloat(g);if(isNaN(k)||0<g.indexOf("%")||0>k)k=f.offsetWidth-parseFloat(window.getComputedStyle(f,null).getPropertyValue("padding-left"))-parseFloat(window.getComputedStyle(f,null).getPropertyValue("padding-right"));b&&(k+=parseFloat(window.getComputedStyle(f,null).getPropertyValue("padding-left"))+
parseFloat(window.getComputedStyle(f,null).getPropertyValue("padding-right")));return h?Math.ceil(k):k},getHeight:function(f,b,h){if(b)return f.offsetHeight;var g=window.getComputedStyle(f,null).getPropertyValue("height"),k=parseFloat(g);if(isNaN(k)||0<g.indexOf("%")||0>k)k=f.offsetHeight-parseFloat(window.getComputedStyle(f,null).getPropertyValue("padding-top"))-parseFloat(window.getComputedStyle(f,null).getPropertyValue("padding-bottom"));b&&(k+=parseFloat(window.getComputedStyle(f,null).getPropertyValue("padding-top"))+
parseFloat(window.getComputedStyle(f,null).getPropertyValue("padding-bottom")));return h?Math.ceil(k):k},getOffset:function(f){var b=f.getBoundingClientRect(),h=document.body,g=f.clientTop||h.clientTop||0,h=f.clientLeft||h.clientLeft||0,k=window.pageYOffset||f.scrollTop;f=window.pageXOffset||f.scrollLeft;document.documentElement&&!window.pageYOffset&&(k=document.documentElement.scrollTop,f=document.documentElement.scrollLeft);return{top:b.top+k-g,left:b.left+f-h}},windowWidth:function(){if(window.innerWidth)return window.innerWidth;
if(document.documentElement&&document.documentElement.clientWidth)return document.documentElement.clientWidth},windowHeight:function(){if(window.innerHeight)return window.innerHeight;if(document.documentElement&&document.documentElement.clientHeight)return document.documentElement.clientHeight},windowScroll:function(){if("undefined"!==typeof pageYOffset)return{left:window.pageXOffset,top:window.pageYOffset};if(document.documentElement)return{left:document.documentElement.scrollLeft,top:document.documentElement.scrollTop}},
addEventListener:function(f,b,h,g){"undefined"===typeof g&&(g=!1);f.addEventListener?f.addEventListener(b,h,g):f.attachEvent&&f.attachEvent("on"+b,h)},removeEventListener:function(f,b,h,g){"undefined"===typeof g&&(g=!1);f.removeEventListener?f.removeEventListener(b,h,g):f.detachEvent&&f.detachEvent("on"+b,h)}},setTransform:function(f,b){var h=f.style;h.webkitTransform=h.MsTransform=h.msTransform=h.MozTransform=h.OTransform=h.transform=b},setTranslate:function(f,b){var h=f.style,g=b.x||0,k=b.y||0,
u=b.z||0;h.webkitTransform=h.MsTransform=h.msTransform=h.MozTransform=h.OTransform=h.transform=this.support.transforms3d?"translate3d("+g+"px,"+k+"px,"+u+"px)":"translate("+g+"px,"+k+"px)";this.support.transforms||(h.left=g+"px",h.top=k+"px")},setTransition:function(f,b){var h=f.style;h.webkitTransitionDuration=h.MsTransitionDuration=h.msTransitionDuration=h.MozTransitionDuration=h.OTransitionDuration=h.transitionDuration=b+"ms"},support:{touch:window.Modernizr&&!0===Modernizr.touch||function(){return!!("ontouchstart"in
window||window.DocumentTouch&&document instanceof DocumentTouch)}(),transforms3d:window.Modernizr&&!0===Modernizr.csstransforms3d||function(){var f=document.createElement("div").style;return"webkitPerspective"in f||"MozPerspective"in f||"OPerspective"in f||"MsPerspective"in f||"perspective"in f}(),transforms:window.Modernizr&&!0===Modernizr.csstransforms||function(){var f=document.createElement("div").style;return"transform"in f||"WebkitTransform"in f||"MozTransform"in f||"msTransform"in f||"MsTransform"in
f||"OTransform"in f}(),transitions:window.Modernizr&&!0===Modernizr.csstransitions||function(){var f=document.createElement("div").style;return"transition"in f||"WebkitTransition"in f||"MozTransition"in f||"msTransition"in f||"MsTransition"in f||"OTransition"in f}(),classList:function(){return"classList"in document.createElement("div").style}()},browser:{ie8:function(){var f=-1;"Microsoft Internet Explorer"===navigator.appName&&null!==(new RegExp(/MSIE ([0-9]{1,}[\.0-9]{0,})/)).exec(navigator.userAgent)&&
(f=parseFloat(RegExp.$1));return-1!==f&&9>f}(),ie10:window.navigator.msPointerEnabled,ie11:window.navigator.pointerEnabled}};(window.jQuery||window.Zepto)&&function(f){f.fn.swiper=function(b){b=new Swiper(f(this)[0],b);f(this).data("swiper",b);return b}}(window.jQuery||window.Zepto);"undefined"!==typeof module&&(module.exports=Swiper);"function"===typeof define&&define.amd&&define([],function(){return Swiper});

(function() {
  $(function(){

  /**
   *  ●●●●●●●●●●
   *  Lightboxs
   *  ●●●●●●●●●●
   */

   /*●●● Scrollbar width detecting ●●●*/
    var scrollWidth = function(){
      var blankDiv = document.createElement("div");
          blankDiv.id = "scrollWidthDetect",
          scrollWidth;
      document.body.appendChild(blankDiv);
      scrollWidth = blankDiv.offsetWidth - blankDiv.clientWidth;
      document.body.removeChild(blankDiv);
      return scrollWidth;
    }();

    $('.btn-auth').on('click', function(){
      $('body').css({'overflow': 'hidden'});
      $('html').css({'paddingRight': scrollWidth});
      $('.lb-bg').css({'overflow-y': 'scroll'});
      $('.lb-bg').fadeIn(400, function(){
        $(this).css('display', 'block');
        $('.lb.login').fadeIn(600);
      });
    });

    $('.lb__close').on('click', function(){
      $('body').css({'overflow': 'visible'});
      $('html').css({'paddingRight': 0});
      $('.lb-bg').css({'overflow-y': 'hidden'});
      $(this).parents('.lb').fadeOut(600, function(){
        $('.lb-bg').fadeOut(400,function(){
        });
      });
    });


  /**
   *  ●●●●●●●●●●
   *  Testdrive page
   *  ●●●●●●●●●●
   */

    $('textarea, input[type="text"]').placeholder();

    /*●●● Sorting ●●●*/
    $('.order__current').on('click', function(){
      var $this = $(this),
          $parent = $this.parent(),
          $menu = $this.next(),
          $items = $menu.children(),
          qty = parseInt($items.length),
          height = parseInt($items.height());
      $menu.css({'top': (qty * height + 1) + 'px'});

      if(!$menu.queue('fx').length){
        $this.toggleClass('clicked');
        $menu.fadeToggle({ 'duration ': 500, 'queue': true });
      }

    });

    $('.btn-showcomponents').on('click', function(){
      $('.components').toggleClass('opened');
    })

  /**
   *  ●●●●●●●●●●
   *  Upload page
   *  ●●●●●●●●●●
   */ 
    $('.custom-file input[type="file"]').on('change', function(){
        var file = $(this).val(),
            $title = $('.custom-file .filename');
            reWin = /.*\\(.*)/,
            fileTitle = file.replace(reWin, "$1"),       //windows filename
            reUnix = /.*\/(.*)/,
            fileTitle = fileTitle.replace(reUnix, "$1"); //unix filename
        $title.text(fileTitle);
    });

    $('.dropdown__current').on('click', function(){
      var $this = $(this),
          $parent = $this.parent(),
          $menu = $this.next();

      if(!$menu.queue('fx').length){
        $this.toggleClass('clicked');
        $menu.fadeToggle({ 'duration ': 500, 'queue': true });
      }

    });

    $('.dropdown__item').on('click', function(){
      var $this = $(this),
          $parent = $this.parent(),
          $current = $('.dropdown__current');
          $input = $('.input-h-ingridient');

      if(!$parent.queue('fx').length){
        $current.text($this.text());
        $input.val($this.data('val'));
        $parent.fadeToggle({ 'duration ': 500, 'queue': true });
      }

    });


  /**
   *  ●●●●●●●●●●
   *  Front page
   *  ●●●●●●●●●●
   */

   if($('.page-main').length){

    /*●●● Front page background slider ●●●*/
    var frontSlider = $('.slider-inner').swiper({
      //initialization
      mode:'horizontal',
      loop: true,
      speed: 900,
      autoplay: false,
      visibilityFullFit: true,
      //Navigation
      keyboardControl: true,
      createPagination: false,
      //Namespace
      wrapperClass: 'slides',
      slideClass: 'slide',
      slideActiveClass: 'active',
      pagination: 'slider_bullets',
      paginationElementClass: 'slider_bullet',
      paginationActiveClass: 'active',
      //Callbacks
      onFirstInit: function(){
        $('.slide-prev').on('click', function(){
          frontSlider.swipePrev();
        });


        $('.slide-next').on('click', function(){
          frontSlider.swipeNext();
        });
      },

    });

   }

  /**
   *  ●●●●●●●●●●
   *  Inner pages slider
   *  ●●●●●●●●●●
   */

   if($('.works-slides-inner').length){

    /*●●● Front page background slider ●●●*/
    var workSlider = $('.works-slides-inner').swiper({
      //initialization
      mode:'horizontal',
      speed: 900,
      loop: true,
      loopedSlides: 3,
      loopAdditionalSlides: 3,
      slidesPerView: 4,
      slidesPerGroup: 3,

      centeredSlides: false,
      offsetPxBefore: 90,

      autoplay: false,
      cssWidthAndHeight:true,
      //Navigation
      keyboardControl: true,
      createPagination: false,
      //Namespace
      wrapperClass: 'works-slides',
      slideClass: 'work-slide',
      //Callbacks
      onFirstInit: function(){
        $('.work-prev').on('click', function(){
          workSlider.swipePrev();
        });


        $('.work-next').on('click', function(){
          workSlider.swipeNext();
        });
      },

    });

   }

  /**
   *  ●●●●●●●●●●
   *  Feeling
   *  ●●●●●●●●●●
   */

   $('.feel').on('click', function(){
    $this = $(this);
    $this.addClass('active').siblings().removeClass('active');
   })

   $('.btn-showfeeling').on('click', function(){
    if($('.feel.active').length) {
        var num = parseInt($('.feel.active').attr('data-feel'));
        $('.feels-wrap').fadeOut(function(){
            $('.feels-boxes').show();
            $('.feel-box').eq(num).fadeIn();
            $(this).parents('.feeling').addClass('clicked');
        });
    }
   });

   $('.btn-closefeel').on('click', function(){
        $('.feel-box:visible').fadeOut(function(){
            $('.feels-boxes').hide();
            $('.feels-wrap').fadeIn();
            $(this).parents('.feeling').removeClass('clicked');
        });
   });

  });
})(jQuery,document)