def delete_from_end(self):
        """Delete and return the data from the last node."""
        if self.head is None:
            return None

        # If there's only one node
        if self.head.get_next() is None:
            data = self.head.get_data()
            self.head = None
            self.length -= 1
            return data

        current = self.head

        # Traverse to the second-to-last node
        while current.get_next().get_next() is not None:
            current = current.get_next()

        data = current.get_next().get_data()
        current.set_next(None)
        self.length -= 1

        return data