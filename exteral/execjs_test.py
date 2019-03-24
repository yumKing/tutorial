import execjs
import os
import binascii
import base64
aes_1 = '''
!function(t,n){"object"==typeof exports?module.exports=exports=n():"function"==typeof define&&define.amd?define([],n):t.CryptoJS=n()}(this,function(){var t=t||function(t,n){var i=Object.create||function(){function t(){}return function(n){var i;return t.prototype=n,i=new t,t.prototype=null,i}}(),e={},r=e.lib={},o=r.Base=function(){return{extend:function(t){var n=i(this);return t&&n.mixIn(t),n.hasOwnProperty("init")&&this.init!==n.init||(n.init=function(){n.$super.init.apply(this,arguments)}),n.init.prototype=n,n.$super=this,n},create:function(){var t=this.extend();return t.init.apply(t,arguments),t},init:function(){},mixIn:function(t){for(var n in t)t.hasOwnProperty(n)&&(this[n]=t[n]);t.hasOwnProperty("toString")&&(this.toString=t.toString)},clone:function(){return this.init.prototype.extend(this)}}}(),s=r.WordArray=o.extend({init:function(t,i){t=this.words=t||[],i!=n?this.sigBytes=i:this.sigBytes=4*t.length},toString:function(t){return(t||c).stringify(this)},concat:function(t){var n=this.words,i=t.words,e=this.sigBytes,r=t.sigBytes;if(this.clamp(),e%4)for(var o=0;o<r;o++){var s=i[o>>>2]>>>24-o%4*8&255;n[e+o>>>2]|=s<<24-(e+o)%4*8}else for(var o=0;o<r;o+=4)n[e+o>>>2]=i[o>>>2];return this.sigBytes+=r,this},clamp:function(){var n=this.words,i=this.sigBytes;n[i>>>2]&=4294967295<<32-i%4*8,n.length=t.ceil(i/4)},clone:function(){var t=o.clone.call(this);return t.words=this.words.slice(0),t},random:function(n){for(var i,e=[],r=function(n){var n=n,i=987654321,e=4294967295;return function(){i=36969*(65535&i)+(i>>16)&e,n=18e3*(65535&n)+(n>>16)&e;var r=(i<<16)+n&e;return r/=4294967296,r+=.5,r*(t.random()>.5?1:-1)}},o=0;o<n;o+=4){var a=r(4294967296*(i||t.random()));i=987654071*a(),e.push(4294967296*a()|0)}return new s.init(e,n)}}),a=e.enc={},c=a.Hex={stringify:function(t){for(var n=t.words,i=t.sigBytes,e=[],r=0;r<i;r++){var o=n[r>>>2]>>>24-r%4*8&255;e.push((o>>>4).toString(16)),e.push((15&o).toString(16))}return e.join("")},parse:function(t){for(var n=t.length,i=[],e=0;e<n;e+=2)i[e>>>3]|=parseInt(t.substr(e,2),16)<<24-e%8*4;return new s.init(i,n/2)}},u=a.Latin1={stringify:function(t){for(var n=t.words,i=t.sigBytes,e=[],r=0;r<i;r++){var o=n[r>>>2]>>>24-r%4*8&255;e.push(String.fromCharCode(o))}return e.join("")},parse:function(t){for(var n=t.length,i=[],e=0;e<n;e++)i[e>>>2]|=(255&t.charCodeAt(e))<<24-e%4*8;return new s.init(i,n)}},f=a.Utf8={stringify:function(t){try{return decodeURIComponent(escape(u.stringify(t)))}catch(t){throw new Error("Malformed UTF-8 data")}},parse:function(t){return u.parse(unescape(encodeURIComponent(t)))}},h=r.BufferedBlockAlgorithm=o.extend({reset:function(){this._data=new s.init,this._nDataBytes=0},_append:function(t){"string"==typeof t&&(t=f.parse(t)),this._data.concat(t),this._nDataBytes+=t.sigBytes},_process:function(n){var i=this._data,e=i.words,r=i.sigBytes,o=this.blockSize,a=4*o,c=r/a;c=n?t.ceil(c):t.max((0|c)-this._minBufferSize,0);var u=c*o,f=t.min(4*u,r);if(u){for(var h=0;h<u;h+=o)this._doProcessBlock(e,h);var p=e.splice(0,u);i.sigBytes-=f}return new s.init(p,f)},clone:function(){var t=o.clone.call(this);return t._data=this._data.clone(),t},_minBufferSize:0}),p=(r.Hasher=h.extend({cfg:o.extend(),init:function(t){this.cfg=this.cfg.extend(t),this.reset()},reset:function(){h.reset.call(this),this._doReset()},update:function(t){return this._append(t),this._process(),this},finalize:function(t){t&&this._append(t);var n=this._doFinalize();return n},blockSize:16,_createHelper:function(t){return function(n,i){return new t.init(i).finalize(n)}},_createHmacHelper:function(t){return function(n,i){return new p.HMAC.init(t,i).finalize(n)}}}),e.algo={});return e}(Math);return t});

!function(e,t,i){"object"==typeof exports?module.exports=exports=t(require("./core.min"),require("./sha1.min"),require("./hmac.min")):"function"==typeof define&&define.amd?define(["./core.min","./sha1.min","./hmac.min"],t):t(e.CryptoJS)}(this,function(e){return function(){var t=e,i=t.lib,r=i.Base,n=i.WordArray,o=t.algo,a=o.MD5,c=o.EvpKDF=r.extend({cfg:r.extend({keySize:4,hasher:a,iterations:1}),init:function(e){this.cfg=this.cfg.extend(e)},compute:function(e,t){for(var i=this.cfg,r=i.hasher.create(),o=n.create(),a=o.words,c=i.keySize,f=i.iterations;a.length<c;){s&&r.update(s);var s=r.update(e).finalize(t);r.reset();for(var u=1;u<f;u++)s=r.finalize(s),r.reset();o.concat(s)}return o.sigBytes=4*c,o}});t.EvpKDF=function(e,t,i){return c.create(i).compute(e,t)}}(),e.EvpKDF});
//# sourceMappingURL=enc-base64.min.js.map

!function(e,t,r){"object"==typeof exports?module.exports=exports=t(require("./core.min"),require("./evpkdf.min")):"function"==typeof define&&define.amd?define(["./core.min","./evpkdf.min"],t):t(e.CryptoJS)}(this,function(e){e.lib.Cipher||function(t){var r=e,i=r.lib,n=i.Base,c=i.WordArray,o=i.BufferedBlockAlgorithm,s=r.enc,a=(s.Utf8,s.Base64),f=r.algo,p=f.EvpKDF,d=i.Cipher=o.extend({cfg:n.extend(),createEncryptor:function(e,t){return this.create(this._ENC_XFORM_MODE,e,t)},createDecryptor:function(e,t){return this.create(this._DEC_XFORM_MODE,e,t)},init:function(e,t,r){this.cfg=this.cfg.extend(r),this._xformMode=e,this._key=t,this.reset()},reset:function(){o.reset.call(this),this._doReset()},process:function(e){return this._append(e),this._process()},finalize:function(e){e&&this._append(e);var t=this._doFinalize();return t},keySize:4,ivSize:4,_ENC_XFORM_MODE:1,_DEC_XFORM_MODE:2,_createHelper:function(){function e(e){return"string"==typeof e?B:x}return function(t){return{encrypt:function(r,i,n){return e(i).encrypt(t,r,i,n)},decrypt:function(r,i,n){return e(i).decrypt(t,r,i,n)}}}}()}),h=(i.StreamCipher=d.extend({_doFinalize:function(){var e=this._process(!0);return e},blockSize:1}),r.mode={}),u=i.BlockCipherMode=n.extend({createEncryptor:function(e,t){return this.Encryptor.create(e,t)},createDecryptor:function(e,t){return this.Decryptor.create(e,t)},init:function(e,t){this._cipher=e,this._iv=t}}),l=h.CBC=function(){function e(e,r,i){var n=this._iv;if(n){var c=n;this._iv=t}else var c=this._prevBlock;for(var o=0;o<i;o++)e[r+o]^=c[o]}var r=u.extend();return r.Encryptor=r.extend({processBlock:function(t,r){var i=this._cipher,n=i.blockSize;e.call(this,t,r,n),i.encryptBlock(t,r),this._prevBlock=t.slice(r,r+n)}}),r.Decryptor=r.extend({processBlock:function(t,r){var i=this._cipher,n=i.blockSize,c=t.slice(r,r+n);i.decryptBlock(t,r),e.call(this,t,r,n),this._prevBlock=c}}),r}(),_=r.pad={},v=_.Pkcs7={pad:function(e,t){for(var r=4*t,i=r-e.sigBytes%r,n=i<<24|i<<16|i<<8|i,o=[],s=0;s<i;s+=4)o.push(n);var a=c.create(o,i);e.concat(a)},unpad:function(e){var t=255&e.words[e.sigBytes-1>>>2];e.sigBytes-=t}},y=(i.BlockCipher=d.extend({cfg:d.cfg.extend({mode:l,padding:v}),reset:function(){d.reset.call(this);var e=this.cfg,t=e.iv,r=e.mode;if(this._xformMode==this._ENC_XFORM_MODE)var i=r.createEncryptor;else{var i=r.createDecryptor;this._minBufferSize=1}this._mode&&this._mode.__creator==i?this._mode.init(this,t&&t.words):(this._mode=i.call(r,this,t&&t.words),this._mode.__creator=i)},_doProcessBlock:function(e,t){this._mode.processBlock(e,t)},_doFinalize:function(){var e=this.cfg.padding;if(this._xformMode==this._ENC_XFORM_MODE){e.pad(this._data,this.blockSize);var t=this._process(!0)}else{var t=this._process(!0);e.unpad(t)}return t},blockSize:4}),i.CipherParams=n.extend({init:function(e){this.mixIn(e)},toString:function(e){return(e||this.formatter).stringify(this)}})),m=r.format={},k=m.OpenSSL={stringify:function(e){var t=e.ciphertext,r=e.salt;if(r)var i=c.create([1398893684,1701076831]).concat(r).concat(t);else var i=t;return i.toString(a)},parse:function(e){var t=a.parse(e),r=t.words;if(1398893684==r[0]&&1701076831==r[1]){var i=c.create(r.slice(2,4));r.splice(0,4),t.sigBytes-=16}return y.create({ciphertext:t,salt:i})}},x=i.SerializableCipher=n.extend({cfg:n.extend({format:k}),encrypt:function(e,t,r,i){i=this.cfg.extend(i);var n=e.createEncryptor(r,i),c=n.finalize(t),o=n.cfg;return y.create({ciphertext:c,key:r,iv:o.iv,algorithm:e,mode:o.mode,padding:o.padding,blockSize:e.blockSize,formatter:i.format})},decrypt:function(e,t,r,i){i=this.cfg.extend(i),t=this._parse(t,i.format);var n=e.createDecryptor(r,i).finalize(t.ciphertext);return n},_parse:function(e,t){return"string"==typeof e?t.parse(e,this):e}}),g=r.kdf={},S=g.OpenSSL={execute:function(e,t,r,i){i||(i=c.random(8));var n=p.create({keySize:t+r}).compute(e,i),o=c.create(n.words.slice(t),4*r);return n.sigBytes=4*t,y.create({key:n,iv:o,salt:i})}},B=i.PasswordBasedCipher=x.extend({cfg:x.cfg.extend({kdf:S}),encrypt:function(e,t,r,i){i=this.cfg.extend(i);var n=i.kdf.execute(r,e.keySize,e.ivSize);i.iv=n.iv;var c=x.encrypt.call(this,e,t,n.key,i);return c.mixIn(n),c},decrypt:function(e,t,r,i){i=this.cfg.extend(i),t=this._parse(t,i.format);var n=i.kdf.execute(r,e.keySize,e.ivSize,t.salt);i.iv=n.iv;var c=x.decrypt.call(this,e,t,n.key,i);return c}})}()});
//# sourceMappingURL=cipher-core.min.js.map
!function(e,i){"object"==typeof exports?module.exports=exports=i(require("./core.min")):"function"==typeof define&&define.amd?define(["./core.min"],i):i(e.CryptoJS)}(this,function(e){!function(){var i=e,t=i.lib,n=t.Base,s=i.enc,r=s.Utf8,o=i.algo;o.HMAC=n.extend({init:function(e,i){e=this._hasher=new e.init,"string"==typeof i&&(i=r.parse(i));var t=e.blockSize,n=4*t;i.sigBytes>n&&(i=e.finalize(i)),i.clamp();for(var s=this._oKey=i.clone(),o=this._iKey=i.clone(),a=s.words,f=o.words,c=0;c<t;c++)a[c]^=1549556828,f[c]^=909522486;s.sigBytes=o.sigBytes=n,this.reset()},reset:function(){var e=this._hasher;e.reset(),e.update(this._iKey)},update:function(e){return this._hasher.update(e),this},finalize:function(e){var i=this._hasher,t=i.finalize(e);i.reset();var n=i.finalize(this._oKey.clone().concat(t));return n}})}()});
//# sourceMappingURL=hmac.min.js.map
!function(e,o,r){"object"==typeof exports?module.exports=exports=o(require("./core.min"),require("./cipher-core.min")):"function"==typeof define&&define.amd?define(["./core.min","./cipher-core.min"],o):o(e.CryptoJS)}(this,function(e){return e.mode.ECB=function(){var o=e.lib.BlockCipherMode.extend();return o.Encryptor=o.extend({processBlock:function(e,o){this._cipher.encryptBlock(e,o)}}),o.Decryptor=o.extend({processBlock:function(e,o){this._cipher.decryptBlock(e,o)}}),o}(),e.mode.ECB});
//# sourceMappingURL=mode-ecb.min.js.map
!function(e,r,i){"object"==typeof exports?module.exports=exports=r(require("./core.min"),require("./cipher-core.min")):"function"==typeof define&&define.amd?define(["./core.min","./cipher-core.min"],r):r(e.CryptoJS)}(this,function(e){return e.pad.Pkcs7});
//# sourceMappingURL=pad-pkcs7.min.js.map
!function(e,r,i){"object"==typeof exports?module.exports=exports=r(require("./core.min"),require("./enc-base64.min"),require("./md5.min"),require("./evpkdf.min"),require("./cipher-core.min")):"function"==typeof define&&define.amd?define(["./core.min","./enc-base64.min","./md5.min","./evpkdf.min","./cipher-core.min"],r):r(e.CryptoJS)}(this,function(e){return function(){var r=e,i=r.lib,n=i.BlockCipher,o=r.algo,t=[],c=[],s=[],f=[],a=[],d=[],u=[],v=[],h=[],y=[];!function(){for(var e=[],r=0;r<256;r++)r<128?e[r]=r<<1:e[r]=r<<1^283;for(var i=0,n=0,r=0;r<256;r++){var o=n^n<<1^n<<2^n<<3^n<<4;o=o>>>8^255&o^99,t[i]=o,c[o]=i;var p=e[i],l=e[p],_=e[l],k=257*e[o]^16843008*o;s[i]=k<<24|k>>>8,f[i]=k<<16|k>>>16,a[i]=k<<8|k>>>24,d[i]=k;var k=16843009*_^65537*l^257*p^16843008*i;u[o]=k<<24|k>>>8,v[o]=k<<16|k>>>16,h[o]=k<<8|k>>>24,y[o]=k,i?(i=p^e[e[e[_^p]]],n^=e[e[n]]):i=n=1}}();var p=[0,1,2,4,8,16,32,64,128,27,54],l=o.AES=n.extend({_doReset:function(){if(!this._nRounds||this._keyPriorReset!==this._key){for(var e=this._keyPriorReset=this._key,r=e.words,i=e.sigBytes/4,n=this._nRounds=i+6,o=4*(n+1),c=this._keySchedule=[],s=0;s<o;s++)if(s<i)c[s]=r[s];else{var f=c[s-1];s%i?i>6&&s%i==4&&(f=t[f>>>24]<<24|t[f>>>16&255]<<16|t[f>>>8&255]<<8|t[255&f]):(f=f<<8|f>>>24,f=t[f>>>24]<<24|t[f>>>16&255]<<16|t[f>>>8&255]<<8|t[255&f],f^=p[s/i|0]<<24),c[s]=c[s-i]^f}for(var a=this._invKeySchedule=[],d=0;d<o;d++){var s=o-d;if(d%4)var f=c[s];else var f=c[s-4];d<4||s<=4?a[d]=f:a[d]=u[t[f>>>24]]^v[t[f>>>16&255]]^h[t[f>>>8&255]]^y[t[255&f]]}}},encryptBlock:function(e,r){this._doCryptBlock(e,r,this._keySchedule,s,f,a,d,t)},decryptBlock:function(e,r){var i=e[r+1];e[r+1]=e[r+3],e[r+3]=i,this._doCryptBlock(e,r,this._invKeySchedule,u,v,h,y,c);var i=e[r+1];e[r+1]=e[r+3],e[r+3]=i},_doCryptBlock:function(e,r,i,n,o,t,c,s){for(var f=this._nRounds,a=e[r]^i[0],d=e[r+1]^i[1],u=e[r+2]^i[2],v=e[r+3]^i[3],h=4,y=1;y<f;y++){var p=n[a>>>24]^o[d>>>16&255]^t[u>>>8&255]^c[255&v]^i[h++],l=n[d>>>24]^o[u>>>16&255]^t[v>>>8&255]^c[255&a]^i[h++],_=n[u>>>24]^o[v>>>16&255]^t[a>>>8&255]^c[255&d]^i[h++],k=n[v>>>24]^o[a>>>16&255]^t[d>>>8&255]^c[255&u]^i[h++];a=p,d=l,u=_,v=k}var p=(s[a>>>24]<<24|s[d>>>16&255]<<16|s[u>>>8&255]<<8|s[255&v])^i[h++],l=(s[d>>>24]<<24|s[u>>>16&255]<<16|s[v>>>8&255]<<8|s[255&a])^i[h++],_=(s[u>>>24]<<24|s[v>>>16&255]<<16|s[a>>>8&255]<<8|s[255&d])^i[h++],k=(s[v>>>24]<<24|s[a>>>16&255]<<16|s[d>>>8&255]<<8|s[255&u])^i[h++];e[r]=p,e[r+1]=l,e[r+2]=_,e[r+3]=k},keySize:8});r.AES=n._createHelper(l)}(),e.AES});
//# sourceMappingURL=aes.min.js.map
!function(e,n){"object"==typeof exports?module.exports=exports=n(require("./core.min")):"function"==typeof define&&define.amd?define(["./core.min"],n):n(e.CryptoJS)}(this,function(e){return e.enc.Utf8});
//# sourceMappingURL=enc-utf8.min.js.map



/* ===================================
 * 加解密工具类
 * Created by Wangcj on 2018/04/24.
 * Copyright 2018 Yooli, Inc.
 * =================================== */
// private property
var keyStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='; // 默认加密key
var highSurrogateMin = 0xd800;
var highSurrogateMax = 0xdbff;
var lowSurrogateMin = 0xdc00;
var lowSurrogateMax = 0xdfff;
var surrogateBase = 0x10000;
var isHighSurrogate = function (charCode) {
	return highSurrogateMin <= charCode && charCode <= highSurrogateMax;
};
var isLowSurrogate = function (charCode) {
	return lowSurrogateMin <= charCode && charCode <= lowSurrogateMax;
};
var combineSurrogate = function (high, low) {
	return ((high - highSurrogateMin) << 10) + (low - lowSurrogateMin) + surrogateBase;
};
var chr = function (charCode) {
	var high, low;
	if (charCode < surrogateBase) {
		return String.fromCharCode(charCode);
	}
	// convert to UTF16 surrogate pair
	high = ((charCode - surrogateBase) >> 10) + highSurrogateMin;
	low = (charCode & 0x3ff) + lowSurrogateMin;
	return String.fromCharCode(high, low);
};

var Crypt = {
	
	/**
	 * private method for UTF-8 encoding
	 * @param string
	 * @returns {string}
	 * @private
	 */
	utf8Encode: function (string) {
		string = string.replace(/\\r\\n/g, '\\n');
		var utfText = '';
		for (var n = 0; n < string.length; n++) {
			var c = string.charCodeAt(n);
			if (c < 128) {
				utfText += String.fromCharCode(c);
			} else if ((c > 127) && (c < 2048)) {
				utfText += String.fromCharCode((c >> 6) | 192);
				utfText += String.fromCharCode((c & 63) | 128);
			} else {
				utfText += String.fromCharCode((c >> 12) | 224);
				utfText += String.fromCharCode(((c >> 6) & 63) | 128);
				utfText += String.fromCharCode((c & 63) | 128);
			}
		}
		return utfText;
	},
	
	/**
	 * private method for UTF-8 decoding
	 * @param utfText
	 * @returns {string}
	 * @private
	 */
	utf8Decode: function (utfText) {
		var string = '';
		var i = 0;
		var c = 0, c2 = 0, c3 = 0;
		while (i < utfText.length) {
			c = utfText.charCodeAt(i);
			if (c < 128) {
				string += String.fromCharCode(c);
				i++;
			} else if ((c > 191) && (c < 224)) {
				c2 = utfText.charCodeAt(i + 1);
				string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
				i += 2;
			} else {
				c2 = utfText.charCodeAt(i + 1);
				c3 = utfText.charCodeAt(i + 2);
				string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
				i += 3;
			}
		}
		return string;
	},
	
	/**
	 * 对字符串进行base64转码
	 * @param input 要转码的字符串
	 * @return String
	 */
	base64Encode: function (input) {
		// public method for encoding
		var output = '';
		var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
		var i = 0;
		input = Crypt.utf8Encode(input);
		while (i < input.length) {
			chr1 = input.charCodeAt(i++);
			chr2 = input.charCodeAt(i++);
			chr3 = input.charCodeAt(i++);
			enc1 = chr1 >> 2;
			enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
			enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
			enc4 = chr3 & 63;
			if (isNaN(chr2)) {
				enc3 = enc4 = 64;
			} else if (isNaN(chr3)) {
				enc4 = 64;
			}
			output = output + keyStr.charAt(enc1) + keyStr.charAt(enc2) + keyStr.charAt(enc3) + keyStr.charAt(enc4);
		}
		return output;
	},
	
	/**
	 * 对base64字符串进行解码
	 * @param input base64字符串
	 * @return String
	 */
	base64Decode: function (input) {
		if (!input) return input;
		// public method for decoding
		var output = '';
		var chr1, chr2, chr3;
		var enc1, enc2, enc3, enc4;
		var i = 0;
		if (!input) input = '';
		input = input.replace(/[^A-Za-z0-9+\/=]/g, '');
		while (i < input.length) {
			enc1 = keyStr.indexOf(input.charAt(i++));
			enc2 = keyStr.indexOf(input.charAt(i++));
			enc3 = keyStr.indexOf(input.charAt(i++));
			enc4 = keyStr.indexOf(input.charAt(i++));
			chr1 = (enc1 << 2) | (enc2 >> 4);
			chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
			chr3 = ((enc3 & 3) << 6) | enc4;
			output = output + String.fromCharCode(chr1);
			if (enc3 !== 64) {
				output = output + String.fromCharCode(chr2);
			}
			if (enc4 !== 64) {
				output = output + String.fromCharCode(chr3);
			}
		}
		output = Crypt.utf8Decode(output);
		return output;
	},
	
	
	/**
	 * Convert JavaScript String to an Array of
	 * UTF8 bytes
	 * @export
	 */
	stringToBytes: function (str) {
		var bytes = [],
			strLength = str.length,
			strIndex = 0,
			charCode, charCode2;
		
		while (strIndex < strLength) {
			charCode = str.charCodeAt(strIndex++);
			
			// handle surrogate pair
			if (isHighSurrogate(charCode)) {
				if (strIndex === strLength) {
					throw new Error('Invalid format');
				}
				charCode2 = str.charCodeAt(strIndex++);
				if (!isLowSurrogate(charCode2)) {
					throw new Error('Invalid format');
				}
				charCode = combineSurrogate(charCode, charCode2);
			}
			
			// convert charCode to UTF8 bytes
			if (charCode < 0x80) {
				// one byte
				bytes.push(charCode);
			} else if (charCode < 0x800) {
				// two bytes
				bytes.push(0xc0 | (charCode >> 6));
				bytes.push(0x80 | (charCode & 0x3f));
			} else if (charCode < 0x10000) {
				// three bytes
				bytes.push(0xe0 | (charCode >> 12));
				bytes.push(0x80 | ((charCode >> 6) & 0x3f));
				bytes.push(0x80 | (charCode & 0x3f));
			} else {
				// four bytes
				bytes.push(0xf0 | (charCode >> 18));
				bytes.push(0x80 | ((charCode >> 12) & 0x3f));
				bytes.push(0x80 | ((charCode >> 6) & 0x3f));
				bytes.push(0x80 | (charCode & 0x3f));
			}
		}
		return bytes;
	},
	
	/**
	 * Convert an Array of UTF8 bytes to
	 * a JavaScript String
	 * @export
	 */
	bytesToString: function (bytes) {
		var str = '',
			length = bytes.length,
			index = 0,
			byte,
			charCode;
		
		while (index < length) {
			// first byte
			byte = bytes[index++];
			if (byte < 0x80) {
				// one byte
				charCode = byte;
			} else if ((byte >> 5) === 0x06) {
				// two bytes
				charCode = ((byte & 0x1f) << 6) | (bytes[index++] & 0x3f);
			} else if ((byte >> 4) === 0x0e) {
				// three bytes
				charCode = ((byte & 0x0f) << 12) | ((bytes[index++] & 0x3f) << 6) | (bytes[index++] & 0x3f);
			} else {
				// four bytes
				charCode = ((byte & 0x07) << 18) | ((bytes[index++] & 0x3f) << 12) | ((bytes[index++] & 0x3f) << 6) | (bytes[index++] & 0x3f);
			}
			str += chr(charCode);
		}
		return str;
	},
	
	/**
	 * 加密（需要先加载lib/aes/aes.min.js文件）
	 * @param plaintText
	 * @param key
	 * @returns {*}
	 */
	encrypt: function (plaintText, key) {
		if (!CryptoJS) {
			alert('CryptoJS no defiend.');
			return;
		}
		if (!key) {
			alert('key no defiend.');
			return;
		}
		
		key = CryptoJS.enc.Utf8.parse(key);
		plaintText = CryptoJS.enc.Utf8.parse(plaintText);
		var encrypted = CryptoJS.AES.encrypt(plaintText, key, {
			mode: CryptoJS.mode.ECB,
			padding: CryptoJS.pad.Pkcs7
		});
		return encrypted.toString();
	},
	
	/**
	 * 字符串转换为十六进制
	 * @returns {string}
	 */
	stringToHex: function (str) {
		if (str === '') return '';
		var hexCharCode = [];
		// hexCharCode.push('0x');
		for (var i = 0; i < str.length; i++) {
			hexCharCode.push((str.charCodeAt(i)).toString(16));
		}
		return hexCharCode.join('');
	},
	
	/**
	 * 十六进制转换为字符串
	 * @returns {string}
	 */
	hexToString: function (hexCharCodeStr) {
		var trimedStr = hexCharCodeStr.trim();
		var rawStr = trimedStr.substr(0, 2).toLowerCase() === '0x' ? trimedStr.substr(2) : trimedStr;
		var len = rawStr.length;
		if (len % 2 !== 0) {
			alert('Illegal Format ASCII Code!');
			return '';
		}
		var curCharCode;
		var resultStr = [];
		for (var i = 0; i < len; i = i + 2) {
			curCharCode = parseInt(rawStr.substr(i, 2), 16); // ASCII Code Value
			resultStr.push(String.fromCharCode(curCharCode));
		}
		return resultStr.join('');
	},
	
	/**
	 * 查找一个字符串中的所有子串的位置
	 * @param str
	 * @param subStr
	 */
	searchSubStr: function (str, subStr) {
		var positions = [];
		var pos = str.indexOf(subStr);
		while (pos > -1) {
			positions.push(pos);
			pos = str.indexOf(subStr, pos + 1);
		}
		return positions;
	},
	
	/**
	 * 格式化数组成员
	 * @param positions
	 * @returns {Array}
	 */
	formatFill: function (positions) {
		var array = [];
		for (var i = 0; i < positions.length; i++) {
			array.push(Number(positions[i]) >= 10 ? positions[i] : '0' + positions[i]);
		}
		return array;
	},
	
	/**
	 * 获取填充字符
	 * @param positions
	 * @returns {string}
	 */
	getFill: function (positions) {
		var str = '';
		for (var i = 0; i < positions.length; i++) {
			str += positions[i];
		}
		return str;
	},
	
	/**
	 * 对加密id和key混合编码
	 * @param loanId
	 * @param enKey 加密key
	 * @returns {string}
	 * d20921210xxxxxxx
	 * d2(第1、2号位): 表示 结尾有两个等(=)号
	 * 09(第3、4号位): 表示 加密后的loanId长度(不含等号)
	 *  9(第5号位): 表示 加密后的loanId中出现的斜杆(/)次数
	 * 02 12(第6～(5号位的值*2 - 1)号位): 表示 斜杆次数对应的补位.(比如：02: 第二号位有个斜杆，第十二号位有个斜杆)
	 *  1(第(5号位的值*2)号位): 表示 加密后的loanId中出现的加号(+)次数
	 * 15: 表示 加号次数对应的补位.(比如：15: 第十五号位有个加号)
	 *
	 * Example
	 *  enLoanId = q5ajtVrfEVfWRsDCWe7Kfg==
	 *  dNum = 2
	 *  enStr = q5ajtVrfEVfWRsDCWe7Kfg
	 *  positions = []
	 *  fill = 00
	 *  key = YjJhZkFpa29jc0ZsbDNXMw==
	 *  k_dNum = 2
	 *  k_enStr = YjJhZkFpa29jc0ZsbDNXMw
	 *  newStr = d2220q5ajtVrfEVfWRsDCWe7Kfgd2YjJhZkFpa29jc0ZsbDNXMw  此为编码后的字符串
	 */
	enCoding: function (loanId, enKey) {
		var deKey = Crypt.base64Decode(enKey); // deKey 解密key
		var enLoanId = Crypt.encrypt(loanId, deKey);
		var dNum = Crypt.searchSubStr(enLoanId, '=').length;
		var enStr = enLoanId.replace(/=/ig, '');
		var positions = Crypt.searchSubStr(enStr, '/');
		enStr = enStr.replace(/\//g, '0'); // 斜杆替换成0(占位)
		positions = Crypt.formatFill(positions);
		var xFill = Crypt.getFill(positions);
		var jPositions = Crypt.searchSubStr(enStr, '+');
		enStr = enStr.replace(/\+/g, '0'); // 加号替换成0(占位)
		jPositions = Crypt.formatFill(jPositions);
		var jFill = Crypt.getFill(jPositions);
		var k_dNum = Crypt.searchSubStr(enKey, '=').length;
		var k_enStr = enKey.replace(/=/ig, '');
		return 'd' + dNum + enStr.length + positions.length + xFill + jPositions.length + jFill + enStr + 'd' + k_dNum + k_enStr;
	}
};


//var key = 'b3VZSDFUcXJwNTI1RjdlMA=='
//var enData = Crypt.encrypt('{"financePlanId":"7573","currentPage":1,"pageSize":10,"date":1553263921083}', 
//                //Crypt.base64Decode(key)
//                'ouYH1Tqrp525F7e0'
//            );
'''

os.environ["EXECJS_RUNTIME"]="PhantomJS"
context = execjs.compile(aes_1)
result = context.eval("Crypt.encrypt('{0}','{1}')".format('{"financePlanId":"7573","currentPage":1,"pageSize":10,"date":1553263921083}', 'ouYH1Tqrp525F7e0'))
# print(context.call("Crypt.encrypt", '{"financePlanId":"7573","currentPage":1,"pageSize":10,"date":1553263921083}', 'ouYH1Tqrp525F7e0'))
print(base64.b64encode(binascii.a2b_hex(result)).decode('utf-8'))


# key = 'ouYH1Tqrp525F7e0'
# datas = {
#     'data': '{"financePlanId":"7573","currentPage":1,"pageSize":10,"date":1553263921083}',
#     'type': 'aes',
#     'arg': 'm=ecb_pad=pkcs7_block=128_p={}_o=0_s=gb2312_t=0'.format(key)
# }
# 
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
#     'Referer': 'http://tool.chacuo.net/cryptaes'
# }
# 
# resp = requests.post('http://tool.chacuo.net/cryptaes', data=datas, headers=headers)
# print(json.loads(resp.text))



