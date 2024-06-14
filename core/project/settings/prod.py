import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://b1cb8b0dedfc439bbca84b264edc562b@sentry.io/1326749",
    integrations=[DjangoIntegration()]
)
