Node* flat(Node* head) {
    Node* curr = head;

    while (true) {
        if (curr->child != nullptr) {
            Node* end = flat(curr->child);

            end->next = curr->next;
            curr->next = curr->child;
            curr->child = nullptr;

            if (end->next == nullptr)
                return end;
        }

        if (curr->next != nullptr)
            curr = curr->next;
        else
            break;
    }

    return curr;
}

Node* flatten(Node* head) {
    Node* curr = head;

    while (true) {
        if (curr->child != nullptr) {
            Node* end = flat(curr->child);

            end->next = curr->next;
            curr->next = curr->child;
            curr->child = nullptr;

            if (end->next == nullptr)
                return end;
        }

        if (curr->next != nullptr)
            curr = curr->next;
        else
            break;
    }

    return head;
}
