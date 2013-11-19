---
title: "Are Google Talk messages signed"
layout: post
categories:
 - Google
 - Prism
 - OTR
---

Lets say [General of Wadiya][aladeen] wants to intercept every message and analyze it. When people start to encrypt them he is storing them so they could be decrypted later when a attack is found or the key is obtained somehow. The people of Wadiya now using [OTR][otr] to communicate without a fear that anybody can prove that this certain conversation ever happened.

For those who don't know OTR. It is a protocol that encrypts the communication, both parties can be sure that nobody intercepts the unencrypted messages and or forging it. They don't sing the message so nobody can blackmail each other or proof that the other party sent the message. Even if some one somehow can encrypt the message, they can't proof that this was the message that was sent. They could have even manipulated it. Because of this, the message could not be used as a evidence in court.

Now Aladeen orders the Chatprovider to sign all messages so he can prove who talked to the opposition and put them in prison. Even if they use [OTR][otr] the counter part of the communication could save the message an blackmail you, because with added signature he can prove that the message is not forged and send by you.

[Thijs][link] pointed out in [his blog post][link] that Google is doing just that. I couldn't believe it. So I installed pidgin and activated the XMPP console plug-in and saw it for my self. I couldn't find the signature when i used the new hangouts. But with an account from a friend who didn't switched yet there was a signature. I sent different strings and when I sent the first one again, I got the same signature again.

I don't know why Google is sining the messages, but this shows again to be careful what you say on the Internet. So just be careful what you write. It might be used against you some day.

[aladeen]: https://en.wikipedia.org/wiki/The_Dictator_(2012_film)
[otr]: https://en.wikipedia.org/wiki/Off-the-Record_Messaging
[link]: https://blog.thijsalkema.de/blog/2013/11/19/is-google-signing-your-chat-messages/