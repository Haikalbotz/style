ó
Þà`c           @   s®   d  d l  Z  d  d l Z d  d l Z d Z d Z d Z d Z d Z d Z d Z	 d	 Z
 d
   Z e  j d  d Z d   Z d   Z d   Z d   Z e d k rª e   n  d S(   iÿÿÿÿNs   [1;97ms   [1;91ms   [1;92ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   [1;90mc         C   sC   x< |  D]4 } t  j j |  t  j j   t j d d  q Wd  S(   Ng      $@id   (   t   syst   stdoutt   writet   flusht   timet   sleep(   t   lolzt   noobs(    (    s   /sdcard/style.pyt   runntxt   s    t   clearsè   [1;97m  _____________ ____ ______
  / _/_ __/\ \/ / / / ____/
  \__ \ / / \ / / / __/   
 ___/ // / / / /___/ /___   
/____//_/ /_/_____/_____/ 
Creator:Ramdhan Ramadhian

[01] Change Termux Display
[02] Install Material
[00] Exit
c          C   s^   t  GHt d  }  |  d k r' t   n3 |  d k r= t   n |  d k rS t   n t   d  S(   Ns   >>> i   i   i    (   t   logot   inputt   ubaht   installt   keluart   main(   t   ramdhan_noobs(    (    s   /sdcard/style.pyR   +   s    


c           C   sW   t  j d  t  j d  t  j d  d GHt j d  t  j d  t  j d  d  S(   Ns   rm $HOME/../usr/etc/bash.bashrcs"   cp -f bash.bashrc $HOME/../usr/etcR	   s#   [1;97mIn Processing Please Wait...i   s   termux-reload-settingst   login(   t   ost   systemR   R   (    (    (    s   /sdcard/style.pyR   7   s    c           C   s?   t  j d  t  j d  t  j d  t  j d  t   d  S(   Ns   pkg install rubys   pkg install toilets   pkg install figlets   gem install lolcat(   R   R   R   (    (    (    s   /sdcard/style.pyR   @   s
    c           C   s   t  j j   d  S(   N(   R   R    t   exit(    (    (    s   /sdcard/style.pyR   G   s    t   __main__(   R   R    R   t   At   Bt   Ct   Dt   Et   Ft   Gt   HR   R   R
   R   R   R   R   t   __name__(    (    (    s   /sdcard/style.pyt   <module>   s&   						