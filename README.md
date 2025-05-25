# mmth.ca
This is the source code repository for the Mastodon link share site, [mmth.ca](https://mmth.ca).
## Why? 
It is hard to link to something on mobile mastodon! Due to mobile web limitations, it's difficult to use the website,
so a variety of apps have sprung up. However, it's difficult to share a link and have it open in the app you like!

Deep linking requires the **sharer** to modify the link to the **specific** app you're using, which varies by app and by
platform. There should be a protocol, `web+federation://` for this, but it's not used, and not all apps support it.
`mastodon://` should be okay, but not all apps support it. So this site was created to help share links between
mastodon users, so you can click a Discord link on mobile and have it open in the app you like.

## How?
We try all the protocols in order.

In the future, Mastodon apps could also register this as a Universal URI domain.

## What do you get out of it?
People can send me links on discord and I can open it without having to jump through like six different login screens.

## Running
`python serve.py`

## Contributing
Open an issue, that's what they're for.

## Hey so there's no license...?
Right. GitHub License for now.