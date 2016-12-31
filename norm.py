"""Data normalization needed for working with fields."""


def field_split(label):
    if "|" in label:
        parts = label.split("|")
    elif ";" in label:
        parts = label.split(";")
    elif "," in label:
        parts = label.split(",")

    labels = []
    for part in parts:
        if part:
            labels.append(part.strip())
    return(labels)
